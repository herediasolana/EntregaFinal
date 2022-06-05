from django.shortcuts import render
from AppNQV.forms import ActoresFormulario, PeliculasFormulario, PlataformasFormulario
from AppNQV.models import Actores, Peliculas, Plataformas

# Create your views here.
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
    plataforma=Plataformas.objects.all()
    context = {'plataformas':plataformas}
    return render (request,'plataformas.html', context=context)


#######################-FORMULARIOS#####################################
def plataformasFormulario(request):
    if request.method=='POST':
        miFormularioPlataformas=PlataformasFormulario(request.POST)
        print(miFormularioPlataformas)

        if miFormularioPlataformas.is_valid:
            informacion =miFormularioPlataformas.cleaned_data

            plataformas = Plataformas ( nombre=informacion['nombre'], 
            duracion=informacion['duracion'], 
            clasificacion=informacion['clasificacion'],
            fechaDeEstreno=informacion['fechaDeEstreno'],
            oscar=informacion['oscar'],
            )
            plataformas.save()
            return render (request,"plataformas.html")
    else:
        miFormularioPlataformas= PlataformasFormulario()
    return render(request, 'plataformasFormulario.html',{'miFormularioPlataformas':miFormularioPlataformas})


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
    if request.method=='POST':
        miFormularioActores=ActoresFormulario(request.POST)
        print(miFormularioActores)

        if miFormularioActores.is_valid:
            informacion =miFormularioActores.cleaned_data

            actores = Actores ( nombre=informacion['nombre'], 
            apellido=informacion['apellido'], 
            edad=informacion['edad'],
            fechaDeNacimiento=informacion['fechaDeNacimiento'],
            )
            plataformas.save()
            return render (request,"actores.html")
    else:
        miFormularioActores= PlataformasFormulario()
    return render(request, 'actoresFormulario.html',{'miFormularioActores':miFormularioActores})