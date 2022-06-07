from django.urls import include, path
from django.contrib import admin
from AppNQV.views import detalle_peliculas, detalle_actores
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
    path('peliculas-Detalle/<int:pk>/', detalle_peliculas, name='detalle_peliculas'),
    path('actores-Detalle/<int:pk>/', detalle_actores, name='detalle_actores'),
    path('plataformas-Detalle/<int:pk>/', views.detalle_plataformas, name='detalle_plataformas'),
]