from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render (request,'home.html')

def peliculas(request):
    return render (request,'peliculas.html')

def actores(request):
    return render (request,'actores.html')

def plataformas(request):
    return render (request,'plataformas.html')