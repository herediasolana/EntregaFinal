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
    nombre: models.CharField(max_length=40)
    duracion: models.TimeField()
    clasificacion: models.CharField(max_length=20, choices=CATEGORIAS, default='drama')
    fechaDeEstreno: models.DateField(blank=True, null=True)
    oscar: models.BooleanField(default=False)
    ratingIMDB: models.IntegerField()
    linkTrailer: models.URLField()

class Actores(models.Model):
    nombre:models.CharField(max_length=40)
    apellido:models.CharField(max_length=40)
    edad:models.IntegerField()
    origen:models.CharField(max_length=40)
    fechaDeNacimiento:models.DateField(blank=True, null=True)

class Plataformas(models.Model):
    cantidadUsuarios:models.IntegerField()
    cantidadPeliculasDisponibles:models.IntegerField()
    precioSuscripcion:models.DecimalField(max_digits=6, decimal_places=2)