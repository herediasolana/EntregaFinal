from django.http import HttpResponse
from django.shortcuts import redirect, render
#- autenticacion
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from EntregaFinal.forms import User_registration_form, User_edit_form

from django.conf import settings
from django.core.mail import send_mail
from usuarios.models import Perfil_usuario


########################## HOME #################################
def index(request):
    print(request.user)
    #print(request.user.perfil_usuario) # no me permite
    print(request.user.is_authenticated)
    return render (request, 'home.html')

def acerca_de(request):
    return render (request, 'extra/acercade.html')

def userPage(request):
    nombre = request.user.username
    context={'nombre':nombre}
    return render(request, 'auth/userPage.html', context=context)

########################## LOGIN #################################
def login_view(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #print(username)
            #print(password)
            user = authenticate(username=username, password=password)
            #print(user)
            if user is not None:
                login(request, user)
                context= {'message': f'Hola {username}!'}
                return render(request, 'home.html',context=context)
                #return redirect
            else:
                context = {'error':'No existe el usuario especificado'}
                form=AuthenticationForm()
                return render(request, 'auth/login.html', context=context)
        else:
            errors=form.errors
            form=AuthenticationForm()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/login.html', context=context)

    else:
        form= AuthenticationForm()
        context = {'form': form}
        return render(request, 'auth/login.html', context=context)

########################## LOGOUT #################################
def logout_view(request):
    logout(request)
    context= {'message': f'Se ha cerrado sesion exitosamente'}
    return render (request,'home.html', context=context)

########################## REGISTER #################################
def register_view(request):
    if request.method =="POST":
        #form = UserCreationForm(request.POST) -->reemplazo el de django por mi formulario creado
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            context= {'message': f'Usuario creado correctamente - {username}'}
            return render(request, 'home.html',context=context)
        else:
            errors=form.errors
            form=User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context=context)

    else:
        form = User_registration_form()
        context = {'form':form}
        return render (request, 'auth/register.html', context=context)

########################## EDIT USER #################################

def edit_user(request):
    #instancia del login
    username = request.user

    if request.method =="POST":
        #form = UserCreationForm(request.POST) -->reemplazo el de django por mi formulario creado
        form = User_edit_form(request.POST)
        
        if form.is_valid():
            form.save()
            context= {'message': f'Usuario actualizado correctamente - {username}'}
            return render(request, 'home.html',context=context)
        else:
            errors=form.errors
            form=User_edit_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/edit_user.html', context=context)

    else:
        form = User_edit_form()
        context = {'form':form}
        return render (request, 'auth/edit_user.html', context=context)

########################## ENVIAR EMAIL #################################
def contacto(request):
    if request.method == 'POST':
        subject=request.POST['asunto']
        message=request.POST['mensaje'] + " " + request.POST['email']
        email_from= settings.EMAIL_HOST_USER
        recipient_list=['herediasolana@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        return render (request, "extra/gracias.html")

    return render(request, 'extra/contacto.html')