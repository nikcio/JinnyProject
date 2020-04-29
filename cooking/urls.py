from django.urls import path
from django.conf.urls import *
from cooking import views as view

urlpatterns = [
    path('', view.Index.as_view(), name="homepage"),
    path('about/', view.About.as_view(), name="about"),
    path('recipes/', view.ViewAll.as_view(), name="recipes"),
    path('recipe/<slug:slug>', view.Detail.as_view(), name="recipe-detail"),
]