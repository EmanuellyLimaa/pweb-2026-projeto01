from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path('equipe/', views.elenco_view, name="elenco"),
    path('sobre/', views.sobre, name="sobre"),
]