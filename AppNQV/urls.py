from django.urls import include, path
from django.contrib import admin

from AppNQV import views
from AppNQV.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home),
    #listados
    path('peliculas', Lista_peliculas.as_view(), name ='peliculas'),#listado peliculas
    path('actores', Lista_actores.as_view(), name ='actores'),#listado actores
    path('plataformas', Lista_plataformas.as_view(), name ='plataformas'),#listado plataformas
    path('datosCuriosos', views.datosCuriosos),#datos curiosos
    #crear formularios
    path('peliculas-formulario', Crear_pelicula.as_view(), name= 'peliculasFormulario'),#crear peliculas
    path('actores-formulario', Crear_actor.as_view(), name= 'actoresFormulario'),#crear actores
    path('plataformas-formulario', Crear_plataforma.as_view(), name= 'plataformasFormulario'),#crear plataformas
    #busquedas
    path('busqueda',views.buscar_view),#pagina de busqueda
    path('resultado',views.random_peli, name='resultado'),
    #detalles
    path('peliculas-detalle/<int:pk>/', views.Detalle_peliculas.as_view(), name='peliculasDetalle'),
    path('actores-detalle/<int:pk>/', views.Detalle_actores.as_view(), name='actoresDetalle'),
    path('plataformas-detalle/<int:pk>/', views.Detalle_plataformas.as_view(), name='plataformaDetalle'),
    #eliminar
    path('plataformas-borrar/<int:pk>/', Delete_plataforma.as_view(), name= 'plataformasBorrar'),
    path('actores-borrar/<int:pk>/', Delete_actores.as_view(), name= 'BorrarActor'),
    path('peliculas-borrar/<int:pk>/', Delete_peliculas.as_view(), name= 'BorrarPelicula'),
    #editar
    #path('plataformas-editar/<int:pk>/', PlataformaEditar.as_view(), name= 'PlataformaEditar'),
    path('plataformas-editar/<int:pk>/', PlataformaEditar.as_view(), name= 'PlataformaEditar'),
    path('actores-editar/<int:pk>/', ActoresEditar.as_view(), name= 'ActoresEditar'),
    path('peliculas-editar/<int:pk>/', PeliculasEditar.as_view(), name= 'peliculasEditar'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)