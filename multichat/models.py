from django.db import models
from tv.models import Movies, Groups
from channels import Group
import json
from Sonder_Blu.settings import MSG_TYPE_MESSAGE


class Room(models.Model):
    title = models.CharField(max_length=255)
    movie_chat = models.OneToOneField(Movies, blank=True, null=True, on_delete=models.SET_NULL)
    group = models.OneToOneField(Groups, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}".format(self.title)

    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("room-%s" % self.id)

    def send_message(self, message, user, msg_type=MSG_TYPE_MESSAGE):
        """
        Called to send a message to the room on behalf of a user.
        """
        final_msg = {'room': str(self.id), 'message': message, 'username': user.username, 'msg_type': msg_type}

        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
