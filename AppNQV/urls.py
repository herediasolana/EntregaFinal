from django.urls import include, path
from django.contrib import admin
from AppNQV import views


urlpatterns = [
    path('home', views.home),
    path('peliculas', views.peliculas),#listado peliculas
    path('actores', views.actores),#listado actores
    path('plataformas', views.plataformas),#listado plataformas
    path('datosCuriosos', views.datosCuriosos),#datos curiosos
    path('peliculasFormulario', views.peliculasFormulario),#formulario peliculas
    path('actoresFormulario', views.actoresFormulario),#formulario actores
    path('plataformasFormulario', views.plataformasFormulario),#formulario plataformas
    path('busqueda',views.buscar_view),#pagina de busqueda
]