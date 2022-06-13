from django.urls import include, path
from django.contrib import admin
from AppNQV.views import detalle_peliculas, detalle_actores, detalle_plataformas
from AppNQV import views
from AppNQV.views import BorrarPlataforma, BorrarActor, BorrarPelicula


urlpatterns = [
    path('home', views.home),
    #listados
    path('peliculas', views.peliculas),#listado peliculas
    path('actores', views.actores),#listado actores
    path('plataformas', views.plataformas),#listado plataformas
    path('datosCuriosos', views.datosCuriosos),#datos curiosos
    #crear formularios
    path('peliculasFormulario', views.peliculasFormulario),#crear peliculas
    path('actoresFormulario', views.actoresFormulario),#crear actores
    path('plataformasFormulario', views.plataformasFormulario),#crear plataformas
    #busquedas
    path('busqueda',views.buscar_view),#pagina de busqueda
    #detalles
    path('peliculas-Detalle/<int:pk>/', detalle_peliculas, name='detalle_peliculas'),
    path('actores-Detalle/<int:pk>/', detalle_actores, name='detalle_actores'),
    path('plataformas-Detalle/<int:pk>/', detalle_plataformas, name='detalle_plataformas'),
    #eliminar
    path('plataformas-borrar/<int:pk>/', BorrarPlataforma, name= 'BorrarPlataforma'),
    path('actores-borrar/<int:pk>/', BorrarActor, name= 'BorrarActor'),
    path('peliculas-borrar/<int:pk>/', BorrarPelicula, name= 'BorrarPelicula'),
]