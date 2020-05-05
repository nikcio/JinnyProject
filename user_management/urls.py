from django.urls import path, include
from django.conf.urls import *
from cooking import models
from django.contrib.auth import views as auth_views
from user_management import views as view
from website.version import v

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
             extra_context={
                 'navigation': models.Navigation.objects.all()[0],
                 'socials': models.Social.objects.all(),
                 'version': v
             },
             redirect_authenticated_user=True)),
    path('logout/',
         auth_views.LogoutView.as_view(
             extra_context={
                 'navigation': models.Navigation.objects.all()[0],
                 'socials': models.Social.objects.all(),
                 'version': v
             })),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             extra_context={
                 'navigation': models.Navigation.objects.all()[0],
                 'socials': models.Social.objects.all(),
                 'version': v
             })),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             extra_context={
                 'navigation': models.Navigation.objects.all()[0],
                 'socials': models.Social.objects.all(),
                 'version': v
             })),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             extra_context={
                 'navigation': models.Navigation.objects.all()[0],
                 'socials': models.Social.objects.all(),
                 'version': v
             })),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             extra_context={
                 'navigation': models.Navigation.objects.all()[0],
                 'socials': models.Social.objects.all(),
                 'version': v
             })),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             extra_context={
                 'navigation': models.Navigation.objects.all()[0],
                 'socials': models.Social.objects.all(),
                 'version': v
             })),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             extra_context={
                 'navigation': models.Navigation.objects.all()[0],
                 'socials': models.Social.objects.all(),
                 'version': v
             })),
    path('', include('django.contrib.auth.urls')),
    path('signup/', view.Signup.as_view(), name='signup'),
    path('dashboard/', view.Dashboard.as_view()),
    path('add/recipe/', view.AddRecipe.as_view()),
    url(r'^update/recipe/(?P<pk>[\w-]+)$', view.UpdateRecipe.as_view(), name='update-recipe')
]
