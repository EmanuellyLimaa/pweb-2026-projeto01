from django.shortcuts import render
from .models import Personagem, Site

def inicio(request):
    site = Site.objects.first()
    return render(request, 'inicio.html', {
        'site': site
    })

def elenco(request):
    personagens = Personagem.objects.all()
    site = Site.objects.first()

    return render(request, 'elenco.html', {
        'personagens': personagens,
        'site': site
    })


def sobre(request):
    site = Site.objects.first()

    return render(request, 'sobre.html', {
        'site': site
    })