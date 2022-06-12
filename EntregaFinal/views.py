from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

##########################LOGIN#################################
def login_view(request):
    if request.method =="POST":
        pass
    else:
        form= AuthenticationForm()
        context = {'form': form}
        return render(request, 'auth/login.html', context=context)



def index(request):
    return render (request, 'home.html')