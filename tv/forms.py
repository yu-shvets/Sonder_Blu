from registration.forms import RegistrationFormUniqueEmail
from django import forms
from .models import Groups, Feedback, Reviews, Movies, UserProfiles
from django.contrib.auth.models import User


class ProfileForm(RegistrationFormUniqueEmail):

    GENDER_CHOICES = (('Female', 'Female'),
                      ('Male', 'Male'))

    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES), max_length=6)
    photo = forms.ImageField(required=False)


class GroupForm(forms.ModelForm):

    def __init__(self, user_id, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        qs = User.objects.exclude(username='admin')
        self.fields['invited'].queryset = qs.exclude(pk=user_id)

    class Meta:
        model = Groups
        exclude = ('author',)


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = ('user',)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        exclude = ('user', 'movie')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfiles
        fields = ('photo',)
