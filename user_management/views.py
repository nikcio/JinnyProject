from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import UpdateView
from user_management import forms
from cooking import models
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from website.version import v


class UpdateRecipe(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'cooking.change_recipe'
    model = models.Recipe
    fields = ['title', 'video', 'description', 'image']
    template_name = 'user_management/update_recipe.html'
    success_url = '/accounts/dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        context['version'] = v
        return context


class AddRecipe(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'cooking.add_recipe'
    template_name = 'user_management/add_recipe.html'
    form_class = forms.RecipeFormSet
    success_url = '/accounts/dashboard/'

    def form_valid(self, form):
        model_instance = form.save(commit=False)
        model_instance.timestamp = timezone.now()
        model_instance.author = self.request.user
        model_instance.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        context['version'] = v
        return context


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'user_management/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        context['allRecipes'] = models.Recipe.objects.order_by("-published")
        context['version'] = v
        return context


class Signup(FormView):
    template_name = 'registration/signup.html'
    form_class = forms.SignUpForm
    success_url = '/accounts/dashboard/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        context['version'] = v
        return context
