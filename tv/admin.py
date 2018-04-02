from django.contrib import admin
from .models import Movies, Reviews, UserProfiles, Category, Groups, Feedback
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Movies)
admin.site.register(Reviews)
admin.site.register(Category)
admin.site.register(Groups)
admin.site.register(Feedback)


class UserProfilesInline(admin.StackedInline):
    model = UserProfiles
    extra = 0


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfilesInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'gender')
    list_select_related = ('profile',)

    def gender(self, instance):
        return instance.profile.gender

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)



