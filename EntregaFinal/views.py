from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
	return HttpResponse('Bienvenidos')

def index(request):
    return render (request, 'index.html')