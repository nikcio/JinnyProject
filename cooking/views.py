from django.shortcuts import render
from django.views.generic import TemplateView
from cooking import models


class Index(TemplateView):
    template_name = "jinny_cooking/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = models.Recipe.objects.all().order_by("-date")[:9]
        return context


class About(TemplateView):
    template_name = "jinny_cooking/about.html"


class Detail(TemplateView):
    template_name = "jinny_cooking/detail.html"


class ViewAll(TemplateView):
    template_name = "jinny_cooking/viewall.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = models.Recipe.objects.all().order_by("-date")

