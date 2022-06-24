from django.contrib import admin
from usuarios.models import Perfil_usuario

@admin.register(Perfil_usuario)
class Perfil_usuario(admin.ModelAdmin):
    list_display = ['usuario','nombre', 'apellido', 'telefono', 'email', 'pais']