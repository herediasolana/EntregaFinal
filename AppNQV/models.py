from random import choices
from secrets import choice
from django.db import models
from django.forms import CharField

# Create your models here.

CATEGORIAS=(
    ('accion', 'ACCION'),
    ('drama','DRAMA'),
    ('suspenso','SUSPENSO'),
    ('terror','TERROR'),
    ('documental','DOCUMENTAL'),
    ('romatica','ROMANTICA'),
)

class Peliculas(models.Model):
    nombre= models.CharField(max_length=40,blank=True, null=True)
    duracion= models.TimeField(blank=True, null=True)
    clasificacion= models.CharField(max_length=20, choices=CATEGORIAS, default='drama')
    fechaDeEstreno= models.DateField(blank=True, null=True)
    oscar= models.BooleanField(default=False)
    ratingIMDB= models.FloatField(blank=True, null=True)
    linkTrailer= models.URLField(blank=True, null=True)

class Actores(models.Model):
    nombre= models.CharField(max_length=40,blank=True, null=True)
    apellido= models.CharField(max_length=40, blank=True, null=True)
    edad= models.IntegerField(blank=True, null=True)
    origen= models.CharField(max_length=40, blank=True, null=True)
    fechaDeNacimiento= models.DateField(blank=True, null=True)

class Plataformas(models.Model):
    nombre= models.CharField(max_length=40,blank=True, null=True)
    cantidadUsuarios=models.IntegerField(blank=True, null=True)
    cantidadPeliculasDisponibles=models.IntegerField(blank=True, null=True)
    precioSuscripcion=models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)