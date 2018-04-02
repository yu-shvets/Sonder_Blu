from registration.backends.default.views import RegistrationView
from .forms import ProfileForm
from .models import UserProfiles


class MyRegistrationView(RegistrationView):

    form_class = ProfileForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        gender = form_class.cleaned_data['gender']
        photo = form_class.cleaned_data['photo']
        if photo:
            photo = self.request.FILES['photo']
            new_profile = UserProfiles.objects.create(user=new_user, gender=gender, photo=photo)
        else:
            new_profile = UserProfiles.objects.create(user=new_user, gender=gender)
        new_profile.save()

        return new_user


