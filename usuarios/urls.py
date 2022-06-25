from django import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from usuarios import views
from usuarios.views import *

urlpatterns = [
    path('detail-user/<int:pk>/', Detalle_usuario.as_view(), name='detail_user'),
    path('edit-profile/<int:pk>/', Editar_usuario.as_view(), name='edit_profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('edit-user/', EditUser.as_view(), name='edit_user'),
    path('delete-user/<slug:username>', delete_user, name='delete_user'),
    path('edit-profile/', EditUser.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name = 'auth/password.html'), name='password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)