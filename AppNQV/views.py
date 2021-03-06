from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse

from AppNQV.models import Actores, Peliculas, Plataformas
from AppNQV.forms import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin #requiere que el usuario este logueado
from django.db.models import Max

import random
from random import Random, choice, random

# Create your views here.

#######################BUSQUEDA#####################################
def buscar_view(request):
    print(request.GET)
    #peliculas = Peliculas.objects.get() #------>lo usamos cuando queremos traer un objeto en particular
    peliculas = Peliculas.objects.filter(nombre__icontains = request.GET['search']) #--->filtra, trae lo que cumple on la condicion
    context = {'peliculas':peliculas}
    return render(request, 'busqueda.html', context = context)

#######################-PAGINAS#####################################

def inicio(request):
    return render (request,'inicio.html')

def home(request):
    return render (request,'home.html')

def datosCuriosos(request):
    return render (request,'datosCuriosos.html')

def success(request):
    return render (request,'extra/success.html')


class Lista_peliculas(ListView):
    model = Peliculas
    template_name = 'peliculas/peliculas.html'


class Lista_actores (ListView):
    model = Actores
    template_name = 'actores/actores.html'

class Lista_plataformas(ListView):
    model = Plataformas
    template_name = 'plataformas/plataformas.html'
    #queryset= Plataformas.objects.filter() #si quiero listar o filtrar los productos que aparezcan



#######################-CREAR #####################################

class Crear_plataforma(LoginRequiredMixin, CreateView):
    model = Plataformas
    template_name = 'plataformas/plataformasFormulario.html'
    form_class = PlataformasFormulario

    def get_success_url(self):
        return reverse('plataformaDetalle', kwargs={'pk':self.object.pk} )

class Crear_pelicula(LoginRequiredMixin, CreateView):
    model = Peliculas
    form_class = PeliculasFormulario
    template_name = 'peliculas/peliculasFormulario.html'
    
    def get_success_url(self):
        return reverse('peliculasDetalle', kwargs={'pk':self.object.pk} )

class Crear_actor(LoginRequiredMixin, CreateView):
    model = Actores
    form_class = ActoresFormulario
    template_name = 'actores/actoresFormulario.html'
        
    def get_success_url(self):
        return reverse('actoresDetalle', kwargs={'pk':self.object.pk} )


########################## ELIMINAR FORMULARIOS ###################################

class Delete_plataforma(LoginRequiredMixin, DeleteView):
    model= Plataformas
    template_name= 'plataformas/plataformasBorrar.html'
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Plataforma eliminada correctamente')
        return reverse('plataformas')

class Delete_actores(LoginRequiredMixin, DeleteView):
    model= Actores
    template_name= 'actores/actoresBorrar.html'
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Actor eliminado correctamente')
        return reverse('actores')

class Delete_peliculas(LoginRequiredMixin, DeleteView):
    model= Peliculas
    template_name= 'peliculas/peliculasBorrar.html'
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Pelicula eliminada correctamente')
        return reverse('peliculas')

############################ DETALLES DE FORMULARIOS ############################

class Detalle_plataformas(DetailView):
    model = Plataformas
    template_name = 'plataformas/plataformaDetalle.html'

class Detalle_actores(DetailView):
    model = Actores
    template_name = 'actores/actoresDetalle.html'

class Detalle_peliculas(DetailView):
    model = Peliculas
    template_name = 'peliculas/peliculasDetalle.html'


############################ MODIFICAR FORMULARIOS  ####################################

class PlataformaEditar(LoginRequiredMixin, UpdateView):
    model = Plataformas
    form_class = PlataformasFormulario
    template_name = 'plataformas/PlataformaEditar.html'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Se han actualizado correctamente los datos')
        return reverse ('plataformas')

class ActoresEditar(LoginRequiredMixin, UpdateView):
    model = Actores
    form_class = ActoresFormulario
    template_name = 'actores/actoresEditar.html'
    

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Se han actualizado correctamente los datos')
        return reverse ('actoresDetalle', kwargs = {'pk':self.object.pk})

class PeliculasEditar(LoginRequiredMixin, UpdateView):
    model = Peliculas
    form_class = PeliculasFormulario
    template_name = 'peliculas/peliculasEditar.html'
    

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Se han actualizado correctamente los datos')
        return reverse ('peliculasDetalle', kwargs = {'pk':self.object.pk})

############################ BOTON PRINCIPAL  ####################################
def random_peli(request):
    peliculas = Peliculas.objects.all()
    pelicula = choice(peliculas)
    resultado_pelicula = Peliculas.objects.filter(nombre=pelicula) #--->filtra, trae lo que cumple on la condicion
    context = {'resultado_pelicula':resultado_pelicula}
    return render(request, 'resultado.html', context = context)

#------------------------------------Crear 

#def plataformasFormulario(request):
#    if request.method=='POST':
#        miFormularioPlataformas=PlataformasFormulario(request.POST)
#        print(miFormularioPlataformas)
#        context = {'message1': 'PLATAFORMA CREADA CORRECTAMENTE'}

#        if miFormularioPlataformas.is_valid:
#            informacion =miFormularioPlataformas.cleaned_data
#
#            plataformas = Plataformas ( nombre=informacion['nombre'], 
#            cantidadUsuarios=informacion['cantidadUsuarios'], 
#            cantidadPeliculasDisponibles=informacion['cantidadPeliculasDisponibles'],
#           precioSuscripcion=informacion['precioSuscripcion'],
#            )
#            plataformas.save()
#            return render (request,"plataformasFormulario.html", context=context)
#    else:
#        miFormularioPlataformas= PlataformasFormulario()
#    return render(request, 'plataformasFormulario.html',{'miFormularioPlataformas':miFormularioPlataformas})

#def peliculasFormulario(request):
#    if request.method=='POST':
#        miFormularioPeliculas=PeliculasFormulario(request.POST)
#        print(miFormularioPeliculas)
#        context = {'message5': 'PELICULA CREADA CORRECTAMENTE'}
#
#        if miFormularioPeliculas.is_valid:
#            informacion =miFormularioPeliculas.cleaned_data
#
#            peliculas = Peliculas ( nombre=informacion['nombre'], 
#            duracion=informacion['duracion'], 
#           clasificacion=informacion['clasificacion'],
#            fechaDeEstreno=informacion['fechaDeEstreno'],
#            oscar=informacion['oscar'],
#            #imagen=informacion['imagen'],
#            )
#            peliculas.save()
#            return render (request,"peliculas.html", context=context)
#    else:
#        miFormularioPeliculas= PeliculasFormulario()
#    return render(request, 'peliculasFormulario.html',{'miFormularioPeliculas':miFormularioPeliculas})

#def actoresFormulario(request):
#    if request.method=='POST':
#        miFormularioActores=ActoresFormulario(request.POST)
#        print(miFormularioActores)
#        context = {'message2': 'ACTOR CREADO/A CORRECTAMENTE'}

#        if miFormularioActores.is_valid:
#            informacion =miFormularioActores.cleaned_data

#            actores = Actores ( nombre=informacion['nombre'], 
#            apellido=informacion['apellido'], 
#            edad=informacion['edad'],
#            origen=informacion['origen'],
#            fechaDeNacimiento=informacion['fechaDeNacimiento'],
#            )
#            actores.save()
#            return render (request,"actores.html", context=context)
#    else:
#        miFormularioActores= ActoresFormulario()
#    return render(request, 'actoresFormulario.html',{'miFormularioActores':miFormularioActores})

#------------------------------------Modificar
# 
# 
# ------------------------------------Borrar 
#def BorrarPlataforma(request, pk):
#    try:
#        if request.method == 'GET':
#            plataforma = Plataformas.objects.get(id=pk)
#           context = {'plataforma': plataforma}
#            return render(request, 'plataformasBorrar.html', context=context)
#        else:
#            plataforma = Plataformas.objects.get(id=pk)
#            plataforma.delete()
#            context = {'message': 'PLATAFORMA ELIMINADA CORRECTAMENTE'}
#            return render(request, 'plataformasBorrar.html', context=context)
#    except:
#        context = {'error': 'Volve a intentar otra vez'}
#        return render(request, 'plataformasFormulario.html', context=context)


#def BorrarActor(request, pk):
#    try:
#        if request.method == 'GET':
#            actores = Actores.objects.get(id=pk)
#            context = {'actores':actores}
#            return render(request, 'actoresBorrar.html', context=context)
#        else:
#            actores = Actores.objects.get(id=pk)
#            actores.delete()
#            context = {'message3': 'ACTOR ELIMINADO/A CORRECTAMENTE'}
#            return render (request, 'actoresBorrar.html', context=context)
#    except:
#        context = {'error': 'Volve a intentar otra vez'}
#        return render(request, 'actoresFormulario.html', context=context)


#def BorrarPelicula(request, pk):
#    try:
##        if request.method == 'GET':
#            pelicula = Peliculas.objects.get(id=pk)
#            context = {'pelicula':pelicula}
#            return render(request, 'peliculasBorrar.html', context=context)
#        else:
#            pelicula = Peliculas.objects.get(id=pk)
#            pelicula.delete()
#            context = {'message4': 'PELICULA ELIMINADA CORRECTAMENTE'}
#            return render (request, 'peliculasBorrar.html', context=context)
#    except:
#        context = {'error': 'La pelicula no existe'}
#        return render(request, 'peliculas.html', context=context)

#------------------------------------Detalle
#def detalle_actores(request, pk):
#    try:
#        actores = Actores.objects.get(id=pk)
#        context = {'actores':actores}
#        return render(request, 'actoresDetalle.html', context=context)
#    except:
#       context = {'error': 'No fue posible encontrar el actor especificado'}
#        return render(request, 'actores.html', context=context)


#def detalle_peliculas(request, pk):
#    try:
#        peliculas = Peliculas.objects.get(id=pk)
#        context = {'peliculas':peliculas}
#        return render(request, 'peliculasDetalle.html', context=context)
#    except:
#        context = {'error': 'No fue posible encontrar la pelicula especificada'}
#        return render(request, 'peliculas.html', context=context)

#def detalle_plataformas(request, pk):
#    try:
#        plataformas = Plataformas.objects.get(id=pk)
#        context = {'plataformas':plataformas}
#        return render(request, 'plataformaDetalle.html', context=context)
#    except:
#        context = {'error': 'No fue posible encontrar la plataforma especificada'}
#        return render(request, 'plataformas.html', context=context)

#------------------------------------Lista
#def actores(request):
#    actores= Actores.objects.all() 
#    context = {'actores': actores}
#    return render (request,'actores.html', context=context)

#def plataformas(request):
#    plataformas=Plataformas.objects.all()
#    context = {'plataformas':plataformas}
#    return render (request,'plataformas.html', context=context)
#def peliculas(request):#funcion
    #de los modelos traeme todos los guardados en la base de datos, lo guardas en clases
#    peliculas= Peliculas.objects.all() 
#    context = {'peliculas': peliculas}
#    return render (request, 'peliculas.html', context=context)