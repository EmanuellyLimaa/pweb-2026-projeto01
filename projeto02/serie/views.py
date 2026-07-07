from django.shortcuts import render
from .models import Personagem, Site

def inicio(request):
    site = Site.objects.first()
    return render(request, 'inicio.html', {
        'site': site
    })
