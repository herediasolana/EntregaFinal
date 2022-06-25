from django.http import HttpResponse
from django.shortcuts import redirect, render
#- autenticacion

from django.conf import settings
from django.core.mail import send_mail



########################## HOME #################################
def index(request):
    print(request.user)
    #print(request.user.perfil_usuario) # no me permite
    print(request.user.is_authenticated)
    return render (request, 'home.html')

def acerca_de(request):
    return render (request, 'extra/acercade.html')

def userPage(request):
    nombre = request.user.username
    context={'nombre':nombre}
    return render(request, 'auth/userPage.html', context=context)

########################## ENVIAR EMAIL #################################
def contacto(request):
    if request.method == 'POST':
        subject=request.POST['asunto']
        message=request.POST['mensaje'] + " " + request.POST['email']
        email_from= settings.EMAIL_HOST_USER
        recipient_list=['herediasolana@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        return render (request, "extra/gracias.html")

    return render(request, 'extra/contacto.html')