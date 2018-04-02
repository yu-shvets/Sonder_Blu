from django.shortcuts import render
from .models import Room


def multichat_view(request):
    rooms = Room.objects.order_by("title")
    return render(request, "multichat/multichat.html", {"rooms": rooms})
