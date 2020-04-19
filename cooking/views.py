from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from django.forms import modelformset_factory
from cooking import models
from cooking import forms
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class Index(TemplateView):
    template_name = "jinny_cooking/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = models.Recipe.objects.filter(published=True).order_by("-date")[:9]
        context['frontpage'] = models.Frontpage.objects.all()[0]
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        return context


class About(TemplateView):
    template_name = "jinny_cooking/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = models.About.objects.all()[0]
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        return context


class Detail(DetailView):
    template_name = "jinny_cooking/detail.html"
    model = models.Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        return context


class ViewAll(TemplateView):
    template_name = "jinny_cooking/viewall.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = models.Recipe.objects.filter(published=True).order_by("-date")
        context['viewall'] = models.ViewAll.objects.all()[0]
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        return context


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = forms.RecipeFormSet(request.POST, request.FILES)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')
    else:
        form = forms.RecipeFormSet()
    return render(request, 'jinny_cooking/add_recipe.html', {'form': form})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = forms.AuthorFormSet(request.POST, request.FILES)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')
    else:
        form = forms.AuthorFormSet()
    return render(request, 'jinny_cooking/add_author.html', {'form': form})


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect('/') #succes
    else:
        pass
        # return error


def logout_user(request):
    logout(request)
