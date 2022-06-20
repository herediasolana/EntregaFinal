from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin #requiere que el usuario este logueado

from usuarios.models import Perfil_usuario

# Create your views here.

class Editar_usuario(LoginRequiredMixin, UpdateView):
    model = Perfil_usuario
    template_name = 'auth/edit_user.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse ('users')

class Detalle_usuario(DetailView):
    model = Perfil_usuario
    template_name = 'auth/detail_user.html'

class Crear_usuario(CreateView):
    model = Perfil_usuario
    template_name = 'auth/register.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse ('user', kwargs = {'pk':self.object.pk})

class Lista_usuarios(ListView):
    model = Perfil_usuario
    template_name = 'auth/users.html'