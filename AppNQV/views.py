from unicodedata import name
from django.shortcuts import render
from AppNQV.forms import ActoresFormulario, PeliculasFormulario, PlataformasFormulario
from AppNQV.models import Actores, Peliculas, Plataformas
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


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

def peliculas(request):#funcion
    #de los modelos traeme todos los guardados en la base de datos, lo guardas en clases
    peliculas= Peliculas.objects.all() 
    context = {'peliculas': peliculas}
    return render (request, 'peliculas.html', context=context)

def actores(request):
    actores= Actores.objects.all() 
    context = {'actores': actores}
    return render (request,'actores.html', context=context)

def plataformas(request):
    plataformas=Plataformas.objects.all()
    context = {'plataformas':plataformas}
    return render (request,'plataformas.html', context=context)



#######################-FORMULARIOS#####################################
def plataformasFormulario(request):
    if request.method=='POST':
        miFormularioPlataformas=PlataformasFormulario(request.POST)
        print(miFormularioPlataformas)
        context = {'massage1': 'PLATAFORMA CREADA CORRECTAMENTE'}

        if miFormularioPlataformas.is_valid:
            informacion =miFormularioPlataformas.cleaned_data

            plataformas = Plataformas ( nombre=informacion['nombre'], 
            cantidadUsuarios=informacion['cantidadUsuarios'], 
            cantidadPeliculasDisponibles=informacion['cantidadPeliculasDisponibles'],
            precioSuscripcion=informacion['precioSuscripcion'],
            )
            plataformas.save()
            return render (request,"plataformasFormulario.html", context=context)
    else:
        miFormularioPlataformas= PlataformasFormulario()
    return render(request, 'plataformasFormulario.html',{'miFormularioPlataformas':miFormularioPlataformas})

def peliculasFormulario(request):
    if request.method=='POST':
        miFormularioPeliculas=PeliculasFormulario(request.POST)
        print(miFormularioPeliculas)
        context = {'massage5': 'PELICULA CREADA CORRECTAMENTE'}

        if miFormularioPeliculas.is_valid:
            informacion =miFormularioPeliculas.cleaned_data

            peliculas = Peliculas ( nombre=informacion['nombre'], 
            duracion=informacion['duracion'], 
            clasificacion=informacion['clasificacion'],
            fechaDeEstreno=informacion['fechaDeEstreno'],
            oscar=informacion['oscar'],
            #imagen=informacion['imagen'],
            )
            peliculas.save()
            return render (request,"peliculas.html", context=context)
    else:
        miFormularioPeliculas= PeliculasFormulario()
    return render(request, 'peliculasFormulario.html',{'miFormularioPeliculas':miFormularioPeliculas})

def actoresFormulario(request):
    if request.method=='POST':
        miFormularioActores=ActoresFormulario(request.POST)
        print(miFormularioActores)
        context = {'massage2': 'ACTOR CREADO/A CORRECTAMENTE'}

        if miFormularioActores.is_valid:
            informacion =miFormularioActores.cleaned_data

            actores = Actores ( nombre=informacion['nombre'], 
            apellido=informacion['apellido'], 
            edad=informacion['edad'],
            origen=informacion['origen'],
            fechaDeNacimiento=informacion['fechaDeNacimiento'],
            )
            actores.save()
            return render (request,"actores.html", context=context)
    else:
        miFormularioActores= ActoresFormulario()
    return render(request, 'actoresFormulario.html',{'miFormularioActores':miFormularioActores})


    ########################## ELIMINAR FORMULARIOS ###################################

def BorrarPlataforma(request, pk):
   try:
       if request.method == 'GET':
         plataforma = Plataformas.objects.get(id=pk)
         context = {'plataforma':plataforma}
         return render(request, 'BorrarPlataforma.html', context=context)
       else:
         plataforma = Plataformas.objects.get(id=pk)
         plataforma.delete()
         context = {'massage': 'PLATAFORMA ELIMINADA CORRECTAMENTE'}
         return render (request, 'plataformasFormulario.html', context=context)
   except:
       context = {'error': 'Volve a intentar otra vez'}
       return render(request, 'plataformasFormulario.html', context=context)


def BorrarActor(request, pk):
   try:
       if request.method == 'GET':
         actores = Actores.objects.get(id=pk)
         context = {'actores':actores}
         return render(request, 'actoresBorrar.html', context=context)
       else:
         actores = Actores.objects.get(id=pk)
         actores.delete()
         context = {'massage3': 'ACTOR ELIMINADO/A CORRECTAMENTE'}
         return render (request, 'actoresFormulario.html', context=context)
   except:
       context = {'error': 'Volve a intentar otra vez'}
       return render(request, 'actoresFormulario.html', context=context)


def BorrarPelicula(request, pk):
   try:
       if request.method == 'GET':
         pelicula = Peliculas.objects.get(id=pk)
         context = {'pelicula':pelicula}
         return render(request, 'peliculasBorrar.html', context=context)
       else:
        pelicula = Peliculas.objects.get(id=pk)
        pelicula.delete()
        context = {'massage4': 'PELICULA ELIMINADA CORRECTAMENTE'}
        return render (request, 'peliculasFormulario.html', context=context)
   except:
       context = {'error': 'Volve a intentar otra vez'}
       return render(request, 'peliculasFormulario.html', context=context)





############################ DETALLES DE FORMULARIOS ############################
def detalle_plataformas(request, pk):
    try:
        plataformas = Plataformas.objects.get(id=pk)
        context = {'plataformas':plataformas}
        return render(request, 'plataformaDetalle.html', context=context)
    except:
        context = {'error': 'Volve a intentar otra vez'}
        return render(request, 'plataformas.html', context=context)

def detalle_actores(request, pk):
    try:
        actores = Actores.objects.get(id=pk)
        context = {'actores':actores}
        return render(request, 'actoresDetalle.html', context=context)
    except:
        context = {'error': 'Volve a intentar otra vez'}
        return render(request, 'actores.html', context=context)


def detalle_peliculas(request, pk):
    try:
        peliculas = Peliculas.objects.get(id=pk)
        context = {'peliculas':peliculas}
        return render(request, 'peliculasDetalle.html', context=context)
    except:
        context = {'error': 'Volve a intentar otra vez'}
        return render(request, 'peliculas.html', context=context)




