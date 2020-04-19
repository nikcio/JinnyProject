from django.urls import path
from cooking import views as view

urlpatterns = [
    path('', view.Index.as_view()),
    path('about/', view.About.as_view()),
    path('recipes/', view.ViewAll.as_view()),
    path('recipe/<slug:slug>', view.Detail.as_view(), name="recipe-detail"),
]