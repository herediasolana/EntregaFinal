"""EntregaFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from EntregaFinal.views import edit_user, index, login_view, logout_view,register_view
#from EntregaFinal.views import saludo, index #ya no seria necesario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ),
    path('AppNQV/', include('AppNQV.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    #path('user/', user_view, name='user'),
    path('edit-user/', edit_user, name='edit_user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#en la carpeta base va la config de url para imagenes
