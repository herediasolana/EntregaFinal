from django.db import models
from django.contrib.auth.models import User

class Perfil_usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'perfil_usuarios')
    telefono= models.CharField(max_length=20, blank=True, null=True)
    email= models.EmailField(blank=True, null=True)
    pais= models.CharField(max_length=30, blank=True, null=True)
    region= models.CharField(max_length=30, blank=True, null=True)
    imagen_perfil= models.ImageField(upload_to='imagen_perfil')

