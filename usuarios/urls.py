from django import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from usuarios import views
from usuarios.views import Detalle_usuario, Editar_usuario, Crear_usuario, login_view, logout_view, register_view, EditUser, PasswordsChangeView


urlpatterns = [
    path('detail-user/', Detalle_usuario.as_view(), name='detail_user'),
    path('edit-user/<int:pk>/', Editar_usuario.as_view(), name='edit_user'),
    path('create-user/', Crear_usuario.as_view(), name='create_user'),
    path('users/', views.Lista_usuarios.as_view(), name='users'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('edit-user/', EditUser.as_view(), name='edit_user'),
    path('password/', PasswordsChangeView.as_view(template_name = 'auth/password.html'), name='password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)