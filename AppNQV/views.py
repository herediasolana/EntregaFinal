from django.http import HttpResponse
from django.shortcuts import render
from AppNQV.forms import PeliculasFormulario

from AppNQV.models import Peliculas

# Create your views here.

def inicio(request):
    return render (request,'inicio.html')

def peliculas(request):
    return render (request,'peliculas.html')

def actores(request):
    return render (request,'actores.html')

def plataformas(request):
    return render (request,'plataformas.html')

def home(request):
    return render (request,'home.html')

def datosCuriosos(request):
    return render (request,'datosCuriosos.html')

def peliculasFormulario(request):
    if request.method=='POST':
        miFormularioPeliculas=PeliculasFormulario(request.POST)
        print(miFormularioPeliculas)

        if miFormularioPeliculas.is_valid:
            informacion =miFormularioPeliculas.cleaned_data

            peliculas = Peliculas ( nombre=informacion['nombre'], 
            duracion=informacion['duracion'], 
            clasificacion=informacion['clasificacion'],
            fechaDeEstreno=informacion['fechaDeEstreno'],
            oscar=informacion['oscar'],
            )
            peliculas.save()
            return render (request,"peliculas.html")
    else:
        miFormularioPeliculas= PeliculasFormulario()
    return render(request, 'peliculasFormulario.html',{'miFormularioPeliculas':miFormularioPeliculas})

def actoresFormulario(request):
    return render(request, 'actoresFormulario.html')