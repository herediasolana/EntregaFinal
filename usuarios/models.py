from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Perfil_usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'profile')
    link =models.URLField(blank=True, null=True)
    bio =models.CharField(max_length=200, blank=True, null=True)
    telefono= models.CharField(max_length=20, blank=True, null=True)
    pais= models.CharField(max_length=30, blank=True, null=True)
    imagen_perfil= models.ImageField(upload_to='imagen_perfil', default='imagen_perfil/perfil_sin_foto.png')
    class Meta:
        verbose_name= 'usuario'
        verbose_name_plural= 'usuarios'
    def __str__(self):
        return str(self.usuario)

@ receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs): #sender es el usuario, instance
    if created:
        Perfil_usuario.objects.create(usuario=instance)
