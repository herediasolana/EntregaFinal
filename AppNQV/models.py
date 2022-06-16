from random import choices
from secrets import choice
from tabnanny import verbose
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
#---------------CLASE-PELICULAS-------------------#
class Peliculas(models.Model):
    nombre= models.CharField(max_length=40,blank=True, null=True)
    duracion= models.IntegerField(blank=True, null=True)
    clasificacion= models.CharField(max_length=20, choices=CATEGORIAS, default='drama')
    fechaDeEstreno= models.DateField(blank=True, null=True, verbose_name= 'Fecha de estreno')
    oscar= models.BooleanField(default=False)
    ratingIMDB= models.FloatField(blank=True, null=True, verbose_name= 'Rating IMDB')
    linkTrailer= models.URLField(blank=True, null=True, verbose_name= 'Link Trailer')
    imagen_peliculas= models.ImageField(upload_to= 'peliculas', blank=True, null=True, verbose_name= 'Imagen Pelicula')
    

    class Meta:
        verbose_name= 'pelicula'
        verbose_name_plural= 'peliculas'

#---------------CLASE-ACTORES-------------------#
class Actores(models.Model):
    nombre= models.CharField(max_length=40,blank=True, null=True)
    apellido= models.CharField(max_length=40, blank=True, null=True)
    edad= models.IntegerField(blank=True, null=True)
    origen= models.CharField(max_length=40, blank=True, null=True)
    fechaDeNacimiento= models.DateField(blank=True, null=True, verbose_name= 'Fecha de Nacimiento')
    imagen_actores= models.ImageField(upload_to= 'actores', blank=True, null=True, verbose_name= 'Imagen Actores')

    class Meta:
        verbose_name= 'actor'
        verbose_name_plural= 'actores'

#---------------CLASE-PLATAFORMAS-------------------#
class Plataformas(models.Model):
    nombre= models.CharField(max_length=40,blank=True, null=True)
    cantidadUsuarios=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de Usuarios')
    cantidadPeliculasDisponibles=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de peliculas disponibles')
    cantidadSeriesDisponibles=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de series disponibles')
    precioSuscripcion=models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name= 'Precio de suscripcion')
    linkPlataforma= models.URLField(blank=True, null=True, verbose_name= 'Link Plataforma')
    imagen_plataformas= models.ImageField(upload_to= 'plataformas', blank=True, null=True, verbose_name= 'Imagen Plataformas')

    class Meta:
        verbose_name= 'plataforma'
        verbose_name_plural= 'plataformas'