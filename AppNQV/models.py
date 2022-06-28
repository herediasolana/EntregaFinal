from datetime import datetime
from email.policy import default
from django.conf import settings
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

CATEGORIAS=(
    ('accion', 'ACCION'),
    ('animada','ANIMADA'),
    ('biografica','BIOGRAFICA'),
    ('comedia','COMEDIA'),
    ('crimen','CRIMEN'),
    ('documental','DOCUMENTAL'),
    ('drama','DRAMA'),
    ('romantica','ROMANTICA'),
    ('suspenso','SUSPENSO'),
    ('terror','TERROR'),
)
def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)   

def year_choices():
    return [(r,r) for r in range(1900, datetime.date.today().year+1)]
#---------------CLASE-PELICULAS-------------------#
class Peliculas(models.Model):
    nombre= models.CharField(max_length=40,blank=True, null=True)
    duracion= models.IntegerField(blank=True, null=True)
    clasificacion= models.CharField(max_length=20, choices=CATEGORIAS, default='drama')
    fechaDeEstreno= models.DateField(blank=True, null=True, verbose_name= 'Fecha de estreno')
    year = models.IntegerField(default=current_year,validators=[MinValueValidator(1900), max_value_current_year], verbose_name= 'año')
    ratingIMDB= models.FloatField(blank=True, null=True, verbose_name= 'Rating IMDB')
    linkTrailer= models.URLField(blank=True, null=True, verbose_name= 'Link Trailer')
    imagen_peliculas= models.ImageField(upload_to= 'peliculas',verbose_name= 'Imagen Pelicula', default='cinema-vector.jpg')
    

    class Meta:
        verbose_name= 'pelicula'
        verbose_name_plural= 'peliculas'
    def __str__(self):
        return self.nombre

#---------------CLASE-ACTORES-------------------#
class Actores(models.Model):
    nombre= models.CharField(max_length=40,blank=True, null=True)
    apellido= models.CharField(max_length=40, blank=True, null=True)
    edad= models.IntegerField(blank=True, null=True)
    origen= models.CharField(max_length=40, blank=True, null=True)
    fechaDeNacimiento= models.DateField(blank=True, null=True, verbose_name= 'Fecha de Nacimiento')
    imagen_actores= models.ImageField(upload_to= 'actores',verbose_name= 'Imagen Actores', default='cinema-vector.jpg')

    class Meta:
        verbose_name= 'actor'
        verbose_name_plural= 'actores'
    def __str__(self):
        return self.nombre + " " + self.apellido
#---------------CLASE-PLATAFORMAS-------------------#
class Plataformas(models.Model):
    nombre= models.CharField(max_length=40,blank=True, null=True)
    cantidadUsuarios=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de Usuarios')
    cantidadPeliculasDisponibles=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de peliculas disponibles')
    cantidadSeriesDisponibles=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de series disponibles')
    precioSuscripcion=models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name= 'Precio de suscripcion')
    linkPlataforma= models.URLField(blank=True, null=True, verbose_name= 'Link Plataforma')
    imagen_plataformas= models.ImageField(upload_to= 'plataformas', verbose_name= 'Imagen Plataformas', default='cinema-vector.jpg')

    class Meta:
        verbose_name= 'plataforma'
        verbose_name_plural= 'plataformas'
    def __str__(self):
        return self.nombre