from django.urls import include, path
from django.contrib import admin

from AppNQV import views
from AppNQV.views import BorrarPlataforma, BorrarActor, BorrarPelicula, PlataformaEditar, ActoresEditar, PeliculasEditar, Lista_plataformas, Crear_pelicula, Crear_actor, Crear_plataforma


urlpatterns = [
    path('home', views.home),
    #listados
    path('peliculas', views.peliculas),#listado peliculas
    path('actores', views.actores),#listado actores
    path('plataformas', Lista_plataformas.as_view(), name ='plataformas'),#listado plataformas
    path('datosCuriosos', views.datosCuriosos),#datos curiosos
    #crear formularios
    path('peliculas-formulario', Crear_pelicula.as_view(), name= 'peliculasFormulario'),#crear peliculas
    path('actores-formulario', Crear_actor.as_view(), name= 'actoresFormulario'),#crear actores
    path('plataformas-formulario', Crear_plataforma.as_view(), name= 'plataformasFormulario'),#crear plataformas
    #busquedas
    path('busqueda',views.buscar_view),#pagina de busqueda
    #detalles
    path('peliculas-detalle/<int:pk>/', views.detalle_peliculas, name='peliculasDetalle'),
    path('actores-detalle/<int:pk>/', views.detalle_actores, name='actoresDetalle'),
    path('plataformas-detalle/<int:pk>/', views.Detalle_plataformas.as_view(), name='plataformaDetalle'),
    #eliminar
    path('plataformas-borrar/<int:pk>/', BorrarPlataforma, name= 'plataformasBorrar'),
    path('actores-borrar/<int:pk>/', BorrarActor, name= 'BorrarActor'),
    path('peliculas-borrar/<int:pk>/', BorrarPelicula, name= 'BorrarPelicula'),
    #editar
    path('plataformas-editar/<int:pk>/', PlataformaEditar.as_view(), name= 'PlataformaEditar'),
    path('actores-editar/<int:pk>/', ActoresEditar.as_view(), name= 'ActoresEditar'),
    path('peliculas-editar/<int:pk>/', PeliculasEditar.as_view(), name= 'peliculasEditar'),
]