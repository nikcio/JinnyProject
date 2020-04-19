from django.urls import path
from cooking import views as view

urlpatterns = [
    path('add/', view.add_recipe),
    path('author/', view.add_author),
    path('login/', view.ViewAll.as_view())
]