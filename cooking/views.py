from django.views.generic import TemplateView, DetailView, ListView
from cooking import models
from website.version import v


class Index(TemplateView):
    template_name = "jinny_cooking/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = models.Recipe.objects.filter(published=True).order_by("-date")[:9]
        context['frontpage'] = models.Frontpage.objects.all()[0]
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        context['version'] = v
        return context


class About(TemplateView):
    template_name = "jinny_cooking/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = models.About.objects.all()[0]
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        context['version'] = v
        return context


class Detail(DetailView):
    template_name = "jinny_cooking/detail.html"
    model = models.Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        context['version'] = v
        return context


class ViewAll(ListView):
    template_name = "jinny_cooking/viewall.html"
    paginate_by = 9
    model = models.Recipe

    def get_queryset(self):
        return models.Recipe.objects.filter(published=True).order_by("-date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['viewall'] = models.ViewAll.objects.all()[0]
        context['navigation'] = models.Navigation.objects.all()[0]
        context['socials'] = models.Social.objects.all()
        context['version'] = v
        return context
