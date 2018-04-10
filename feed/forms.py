from django import forms
from .models import Posts, Comments, Messages


class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        exclude = ('user', 'likes')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment',)


class MessageForm(forms.ModelForm):

    class Meta:
        model = Messages
        fields = ('message',)
