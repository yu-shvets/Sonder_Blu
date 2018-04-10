from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect, reverse
from django.views.generic import TemplateView, DetailView
from .models import Movies, Groups, Feedback, Reviews, UserProfiles, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from friendship.models import Friend, FriendshipRequest
from django.views.generic.edit import CreateView, UpdateView
from .forms import GroupForm, FeedbackForm, ReviewForm, UserProfileForm, UserForm
from django.urls import reverse_lazy
from django.contrib import messages
from multichat.models import Room
from django_filters import FilterSet, ModelMultipleChoiceFilter, OrderingFilter
from django import forms
from django_filters.views import FilterView
from datetime import datetime, timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from feed.forms import MessageForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['movies'] = Movies.objects.all()
        context['groups'] = Groups.objects.all()
        context['feedback_form'] = FeedbackForm
        context['feedbacks'] = Feedback.objects.all()
        context['review_form'] = ReviewForm
        context['timediff'] = timediff()
        if not self.request.user.is_anonymous:
            context['sent_requests'] = [item.to_user for item in Friend.objects.sent_requests(user=self.request.user)]
        return context


class SearchView(TemplateView):
    template_name = 'tv/search.html'


def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    unread_requests = [item.from_user for item in Friend.objects.unread_requests(user=user)]
    friends = Friend.objects.friends(user)
    messageform = MessageForm
    userprofileform = UserProfileForm
    userform = UserForm
    return render(request, 'registration/profile.html', {'user_info': user, 'unread_requests': unread_requests,
                                                         'friends': friends, 'messageform': messageform,
                                                         'userform': userform, 'userprofileform': userprofileform})


def search(request):
    query = request.GET.get('query').strip()
    movies = Movies.objects.filter(name__icontains=query)
    people = User.objects.filter(username__icontains=query)
    return render(request, 'base.html', {'movies': movies, 'people': people, 'query': query})


def search_movies(request, query):
    movies = Movies.objects.filter(name__icontains=query)
    return render(request, 'base.html', {'movies': movies, 'query': query})


def search_people(request, query):
    people = User.objects.filter(username__icontains=query)
    return render(request, 'base.html', {'people': people, 'query': query})


@login_required()
def like(request):
    movie_id = request.GET.get('movie_id', None)
    movie = get_object_or_404(Movies, id=movie_id)
    user = request.user
    if movie.likes.filter(id=user.id).exists():
        movie.likes.remove(user)
    else:
        movie.likes.add(user)
    return HttpResponse(movie.total_likes)


def send_request(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    Friend.objects.add_friend(request.user, other_user)
    return HttpResponseRedirect(reverse('home'))


def accept_request(request, user_id):
    friend_request = FriendshipRequest.objects.get(from_user=user_id, to_user=request.user)
    friend_request.accept()
    return HttpResponseRedirect(reverse('home'))


def cancel_request(request, user_id):
    friend_request = FriendshipRequest.objects.get(from_user=user_id, to_user=request.user)
    friend_request.cancel()
    return HttpResponseRedirect(reverse('home'))


def remove_friend(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    Friend.objects.remove_friend(request.user, other_user)
    return HttpResponseRedirect(reverse('home'))


class GroupFormView(TemplateView):
    template_name = 'tv/group_form.html'

    def get_context_data(self, **kwargs):
        context = super(GroupFormView, self).get_context_data(**kwargs)
        context['form'] = GroupForm(user_id=self.request.user.pk)
        return context


class GroupCreateView(CreateView):
    model = Groups
    fields = ('name', 'movie', 'invited')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        form.save_m2m()
        room = Room(title=obj.name, group=obj)
        room.save()
        return HttpResponseRedirect(reverse('home'))


class GroupDetailView(DetailView):
    model = Groups
    template_name = 'tv/groups.html'


def join_group(request, group_id):
    group = get_object_or_404(Groups, pk=group_id)
    group.invited.add(request.user)
    return HttpResponseRedirect(reverse('group', kwargs={'pk': group_id}))


def leave_group(request, group_id):
    group = get_object_or_404(Groups, pk=group_id)
    group.invited.remove(request.user)
    return HttpResponseRedirect(reverse('group', kwargs={'pk': group_id}))


def delete_group(request, group_id):
    group = get_object_or_404(Groups, pk=group_id)
    group.delete()
    return HttpResponseRedirect(reverse('home'))


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('home'))


class ReviewCreateView(CreateView):
    model = Reviews
    form_class = ReviewForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.movie = Movies.objects.get(pk=self.kwargs['movie_id'])
        obj.save()
        return HttpResponseRedirect(reverse('home'))

    def form_invalid(self, form):
        messages.error(self.request,
                       "Please, submit video file, that should not exceed 10 MB.")
        return HttpResponseRedirect(reverse('home'))


class ReviewUpdateView(UpdateView):
    model = Reviews
    fields = ['video', 'review']
    template_name = 'tv/review_update_form.html'
    success_url = reverse_lazy('home')


def add_favorite(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    userprofile = UserProfiles.objects.get(user=request.user)
    userprofile.favorites.add(movie)
    return HttpResponseRedirect(reverse('home'))


class CategoryFilter(FilterSet):

    category = ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    rating = ModelMultipleChoiceFilter(queryset=Movies.objects.values_list('rating', flat=True), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Movies
        fields = ['category', 'rating']


class CategoryFilterView(FilterView):
    template_name = 'tv/category_search.html'
    filterset_class = CategoryFilter


def timediff():
    movie = Movies.objects.last()
    timediff = datetime.now(timezone.utc) - movie.showtime
    return int(timediff.total_seconds())


def user_edit(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if all([user_form.is_valid(), profile_form.is_valid()]):
            user = user_form.save()
            profile = profile_form.save()
            return HttpResponseRedirect(reverse('home'))

    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'tv/profile_update_form.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


class UpdateFormView(TemplateView):
    template_name = 'tv/profile_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateFormView, self).get_context_data(**kwargs)
        context['user_form'] = UserForm(instance=self.request.user)
        context['profile_form'] = UserProfileForm(instance=self.request.user.profile)
        return context