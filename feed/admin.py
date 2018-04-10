from django.contrib import admin
from .models import Posts, Comments, Feeds, Messages

admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Feeds)
admin.site.register(Messages)