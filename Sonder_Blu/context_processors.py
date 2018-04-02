from django.contrib.auth.models import User
from friendship.models import Friend


def project_variables(request):
    users = User.objects.all()
    if not request.user.is_anonymous:
        unread_requests = [item.from_user for item in Friend.objects.unread_requests(user=request.user)]
        friends = Friend.objects.friends(request.user)
        return {'users': users, 'unread_requests': unread_requests, 'friends': friends}
    return {'users': users}
