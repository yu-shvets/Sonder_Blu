from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, HttpResponse
from .models import Posts, Comments, Feeds, Messages
from friendship.models import Friend, FriendshipRequest
from django.views.generic.edit import CreateView
from .forms import PostForm, CommentForm, MessageForm
from django.contrib.auth.models import User
from feed.forms import MessageForm


def feed_view(request):
    feed = Feeds.objects.filter(user=request.user).first()
    postform = PostForm
    commentform = CommentForm
    new_messages = Messages.objects.filter(to_user=request.user, read_status=False)
    read_messages = Messages.objects.filter(to_user=request.user, read_status=True)
    return render(request, 'feed/feed.html', {'feed': feed, 'postform': postform, 'commentform': commentform,
                                              'new_messages': new_messages, 'read_messages': read_messages})


class PostCreateView(CreateView):
    form_class = PostForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('feed'))


class CommentCreateView(CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.post = Posts.objects.get(pk=self.kwargs['post_id'])
        obj.save()
        return HttpResponseRedirect(reverse('feed'))


class AnswerCreateView(CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        comment = Comments.objects.get(pk=self.kwargs['comment_id'])
        obj.post = comment.post
        obj.parent = comment
        obj.save()
        return HttpResponseRedirect(reverse('feed'))


def post_like(request):
    post_id = request.GET.get('post_id', None)
    post = get_object_or_404(Posts, id=post_id)
    user = request.user
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return HttpResponse(post.total_likes)


def comment_like(request):
    comment_id = request.GET.get('node_id', None)
    comment = get_object_or_404(Comments, id=comment_id)
    user = request.user
    if comment.likes.filter(id=user.id).exists():
        comment.likes.remove(user)
    else:
        comment.likes.add(user)
    return HttpResponse(comment.total_likes)


class MessageCreateView(CreateView):
    form_class = MessageForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.from_user = self.request.user
        obj.to_user = User.objects.get(pk=self.kwargs['user_id'])
        obj.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


def open_message(request, message_id):
    message = Messages.objects.get(pk=message_id)
    if message.read_status == False:
        message.read_status = True
        message.save()
    messageform = MessageForm
    return render(request, 'feed/private_message.html', {'message': message, 'messageform': messageform})
