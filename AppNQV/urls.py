from django.urls import include, path
from django.contrib import admin
from AppNQV import views


urlpatterns = [
    path('home', views.home),
    path('peliculas', views.peliculas),
    path('actores', views.actores),
    path('plataformas', views.plataformas),
    path('datosCuriosos', views.datosCuriosos),
]