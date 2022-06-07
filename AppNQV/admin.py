from django.contrib import admin
from AppNQV.models import Actores, Peliculas, Plataformas


# Register your models here.

@admin.register(Actores)
class ActoresAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'edad', 'fechaDeNacimiento']

@admin.register(Peliculas)
class PeliculasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'duracion', 'clasificacion', 'fechaDeEstreno']

@admin.register(Plataformas)
class PlataformasAdmin(admin.ModelAdmin):
    list_display = ['nombre','cantidadUsuarios', 'precioSuscripcion', 'cantidadPeliculasDisponibles']
