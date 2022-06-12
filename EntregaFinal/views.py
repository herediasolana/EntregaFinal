from django.http import HttpResponse
from django.shortcuts import redirect, render
#- autenticacion
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

########################## HOME #################################
def index(request):
    print(request.user)
    print(request.user.is_authenticated)
    return render (request, 'home.html')

########################## LOGIN #################################
def login_view(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #print(username)
            #print(password)
            user = authenticate(username=username, password=password)
            #print(user)
            if user is not None:
                login(request, user)
                context= {'message': f'Hola {username}!'}
                return render(request, 'home.html',context=context)
                #return redirect
            else:
                context = {'error':'No existe el usuario especificado'}
                form=AuthenticationForm()
                return render(request, 'auth/login.html', context=context)
        else:
            errors=form.errors
            form=AuthenticationForm()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/login.html', context=context)

    else:
        form= AuthenticationForm()
        context = {'form': form}
        return render(request, 'auth/login.html', context=context)

########################## LOGOUT #################################
def logout_view(request):
    logout(request)
    context= {'message': f'Se ha cerrado sesion exitosamente'}
    return render (request,'home.html', context=context)