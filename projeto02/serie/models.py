from django.db import models

class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    posicao = models.CharField(max_length=100)
    nascimento = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='integrantes/')

    def __str__(self):
        return self.nome
    
class Site(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    historia = models.TextField()
    autores = models.CharField(max_length=200)
    copyright = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    