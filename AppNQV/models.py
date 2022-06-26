from email.policy import default
from django.db import models

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