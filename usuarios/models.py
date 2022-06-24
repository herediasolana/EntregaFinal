from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.dispatch import receiver
from django.db.models.signals import post_save

def user_directory_path(instance, filename):
    return 'imagen_perfil/{0}/{1}'.format(instance.user.id, filename)


class Perfil_usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'perfil_usuarios')
    nombre =models.CharField(max_length=20)
    apellido =models.CharField(max_length=20)
    telefono= models.CharField(max_length=20, blank=True, null=True)
    email= models.EmailField(blank=True, null=True)
    pais= models.CharField(max_length=30, blank=True, null=True)
    imagen_perfil= models.ImageField(upload_to=user_directory_path, default='imagen_perfil/perfil_sin_foto.png')

    class Meta:
        verbose_name= 'usuario'
        verbose_name_plural= 'usuarios'

@ receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs): #sender es el usuario, instance
    if created:
        Perfil_usuario.objects.create(usuario=instance)
