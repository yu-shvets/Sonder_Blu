from django.db import models
from django.contrib.auth.models import User
from tv.models import CommonInfo


class ChatMessage(CommonInfo):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=3000)
    message_html = models.TextField()

    class Meta(object):
        verbose_name = "Chat message"
        verbose_name_plural = "Chat messages"

    def __str__(self):
        return self.message
