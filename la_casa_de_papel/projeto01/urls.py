from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path('equipe/', views.views.elenco, name="elenco"),
    path('sobre/', views.sobre, name="sobre"),
]