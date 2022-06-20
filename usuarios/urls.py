from django import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path
from django.contrib import admin

from usuarios import views
from usuarios.views import Detalle_usuario, Editar_usuario, Crear_usuario

urlpatterns = [
    path('detail-user/<int:pk>/', views.Detalle_usuario.as_view(), name='detail_user'),
    path('edit-user/<int:pk>/', views.Editar_usuario.as_view(), name='edit_user'),
    path('create-user/', views.Crear_usuario.as_view(), name='create_user'),
    path('users/', views.Lista_usuarios.as_view(), name='users'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)