"""Sonder_Blu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import reverse_lazy
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from tv.views import HomeView, search, like, send_request, accept_request, cancel_request, remove_friend, profile, \
    GroupFormView, GroupCreateView, GroupDetailView, join_group, leave_group, delete_group, FeedbackCreateView, \
    ReviewCreateView, search_movies, search_people, add_favorite, CategoryFilterView, ReviewUpdateView, user_edit, \
    UpdateFormView, SearchView, FilmView, ProfileView, GroupView
from chat.views import IndexView
from multichat.views import multichat_view
from feed.views import feed_view, PostCreateView, CommentCreateView, post_like, AnswerCreateView, comment_like, \
    MessageCreateView, open_message
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import RedirectView, TemplateView
from tv.regbackend import MyRegistrationView
from registration.backends.default.views import ActivationView, RegistrationView, ResendActivationView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^search_view/$', SearchView.as_view(), name='search_view'),
    url(r'^film_view/$', FilmView.as_view(), name='film_view'),
    url(r'^profile_view/$', ProfileView.as_view(), name='profile_view'),
    url(r'^group_view/$', GroupView.as_view(), name='group_view'),

    url(r'^search/$', search, name='search'),
    url(r'^like/$', like, name='like'),
    url(r'^send_request/(?P<user_id>\d+)/$', send_request, name='send_request'),
    url(r'^accept_request/(?P<user_id>\d+)/$', accept_request, name='accept_request'),
    url(r'^cancel_request/(?P<user_id>\d+)/$', cancel_request, name='cancel_request'),
    url(r'^remove_friend/(?P<user_id>\d+)/$', remove_friend, name='remove_friend'),
    url(r'^group_form/$', GroupFormView.as_view(), name='group_form'),
    url(r'^group_create/$', GroupCreateView.as_view(), name='group_create'),
    url(r'^group/(?P<pk>\d+)/$', GroupDetailView.as_view(), name='group'),
    url(r'^join_group/(?P<group_id>\d+)/$', join_group, name='join_group'),
    url(r'^leave_group/(?P<group_id>\d+)/$', leave_group, name='leave_group'),
    url(r'^delete_group/(?P<group_id>\d+)/$', delete_group, name='delete_group'),
    url(r'^feedback_create/$', FeedbackCreateView.as_view(), name='feedback_create'),
    url(r'^review_create/(?P<movie_id>\d+)/$', ReviewCreateView.as_view(), name='review_create'),
    url(r'^search_movies/(?P<query>.+)/$', search_movies, name='search_movies'),
    url(r'^search_people/(?P<query>.+)/$', search_people, name='search_people'),
    url(r'^add_favorite/(?P<movie_id>\d+)/$', add_favorite, name='add_favorite'),
    url(r'^category_search/$', CategoryFilterView.as_view(), name='category_search'),
    url(r'^review_update/(?P<pk>\d+)/$', ReviewUpdateView.as_view(), name='review_update'),
    url(r'^user_update/$', user_edit, name='user_update'),
    url(r'^update_form/$', UpdateFormView.as_view(), name='update_form'),

                  url(r'^login/$',
                      auth_views.LoginView.as_view(
                          template_name='registration/login.html'),
                      name='auth_login'),
                  url(r'^logout/$',
                      auth_views.LogoutView.as_view(
                          template_name='registration/logout.html'),
                      name='auth_logout'),
                  url(r'^accounts/register/$',
                      MyRegistrationView.as_view(),
                      name='registration_register'),
                  url(r'^accounts/profile/(?P<user_id>\d+)/$', profile, name='profile'),

                  url(r'^password/change/$',
                      auth_views.PasswordChangeView.as_view(
                          success_url=reverse_lazy('auth_password_change_done')),
                      name='auth_password_change'),
                  url(r'^password/change/done/$',
                      auth_views.PasswordChangeDoneView.as_view(),
                      name='auth_password_change_done'),
                  url(r'^password/reset/$',
                      auth_views.PasswordResetView.as_view(
                          success_url=reverse_lazy('auth_password_reset_done')),
                      name='auth_password_reset'),
                  url(r'^password/reset/complete/$',
                      auth_views.PasswordResetCompleteView.as_view(),
                      name='auth_password_reset_complete'),
                  url(r'^password/reset/done/$',
                      auth_views.PasswordResetDoneView.as_view(),
                      name='auth_password_reset_done'),
                  url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                      auth_views.PasswordResetConfirmView.as_view(
                          success_url=reverse_lazy('auth_password_reset_complete')),
                      name='password_reset_confirm'),

                  url(r'^activate/complete/$',
                      TemplateView.as_view(template_name='registration/activation_complete.html'),
                      name='registration_activation_complete'),
                  url(r'^activate/resend/$',
                      ResendActivationView.as_view(),
                      name='registration_resend_activation'),
                  # Activation keys get matched by \w+ instead of the more specific
                  # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
                  # that way it can return a sensible "invalid key" message instead of a
                  # confusing 404.
                  url(r'^activate/(?P<activation_key>\w+)/$',
                      ActivationView.as_view(),
                      name='registration_activate'),
                  url(r'^register/complete/$',
                      TemplateView.as_view(template_name='registration/registration_complete.html'),
                      name='registration_complete'),
                  url(r'^register/closed/$',
                      TemplateView.as_view(template_name='registration/registration_closed.html'),
                      name='registration_disallowed'),


    url(r'^accounts/', include('registration.backends.default.urls', namespace='accounts')),

    url(r'^chat/$', IndexView.as_view(), name='chat'),

    url(r'^multichat/$', multichat_view, name='multichat'),

    url(r'^feed/$', feed_view, name='feed'),
    url(r'^create_post/$', PostCreateView.as_view(), name='create_post'),
    url(r'^create_comment/(?P<post_id>\d+)/$', CommentCreateView.as_view(), name='create_comment'),
    url(r'^create_answer/(?P<comment_id>\d+)/$', AnswerCreateView.as_view(), name='create_answer'),
    url(r'^feed/post_like/$', post_like, name='post_like'),
    url(r'^feed/comment_like/$', comment_like, name='comment_like'),
    url(r'^message_create/(?P<user_id>\d+)/$', MessageCreateView.as_view(), name='message_create'),
    url(r'^open_message/(?P<message_id>\d+)/$', open_message, name='open_message'),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
