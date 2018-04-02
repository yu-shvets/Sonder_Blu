from django.db.models.signals import post_save
from django.dispatch import receiver
from tv.models import Movies
from multichat.models import Room


@receiver(post_save, sender=Movies)
def create_favorites(sender, instance, created, **kwargs):
    if created:
        Room.objects.create(title=instance.name, movie_chat=instance)