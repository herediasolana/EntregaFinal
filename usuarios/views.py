from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin #requiere que el usuario este logueado
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView

from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from usuarios.forms import User_registration_form, User_edit_form, Password_change_form
from usuarios.models import Perfil_usuario
# Create your views here.

class Editar_usuario(LoginRequiredMixin, UpdateView):
    model = Perfil_usuario
    template_name = 'auth/edit_profile.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse ('userPage')

class Detalle_usuario(DetailView):
    model = Perfil_usuario
    template_name = 'auth/detail_user.html'

    def get_context_data(self, *args, **kwargs):
        profiles= Perfil_usuario.objects.all()
        context= super(Detalle_usuario, self).get_context_data(*args, **kwargs)
        
        page_user=get_object_or_404(Perfil_usuario, id=self.kwargs['pk'])

        context['page_user']=page_user
        return context

class Crear_usuario(CreateView):
    model = Perfil_usuario
    template_name = 'auth/register.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse ('user', kwargs = {'pk':self.object.pk})

class Lista_usuarios(ListView):
    model = Perfil_usuario
    template_name = 'auth/users.html'


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
class EditUser(generic.UpdateView):
    form_class = User_edit_form
    template_name = 'auth/edit_user.html'
    def get_object(self):
        return self.request.user
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Usuario actualizado correctamente')
        return reverse ('userPage')

class PasswordsChangeView(PasswordChangeView):
    form_class: Password_change_form
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Contraseña actualizada correctamente')
        return reverse ('userPage')

def delete_user(request, username):
    try:
        u=User.objects.get(username=username)
        u.delete()
        context= {'message': f'Usuario eliminado correctamente - {username}'}
    except User.DoesNotExist:
        messages.error(request, 'El usuario no existe')
        return render (request, 'home.html')
    except Exception as e: 
        return render(request, 'home.html',{'err':e.message})

    return render(request, 'home.html', context=context) 

#def edit_user(request):
#    #instancia del login
#    username = request.user
#
#    if request.method =="POST":
#        #form = UserCreationForm(request.POST) -->reemplazo el de django por mi formulario creado
#        form = User_edit_form(request.POST)
#        
#        if form.is_valid():
 #           form.save()
#            context= {'message': f'Usuario actualizado correctamente - {username}'}
#            return render(request, 'home.html',context=context)
#        else:
#            errors=form.errors
#            form=User_edit_form()
#            context = {'errors':errors, 'form':form}
#            return render(request, 'auth/edit_user.html', context=context)

#    else:
#        form = User_edit_form()
#        context = {'form':form}
 #       return render (request, 'auth/edit_user.html', context=context)