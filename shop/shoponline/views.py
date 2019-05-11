from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
from .models import *


def login(request):
	return render(request, 'shoponline/login.html', {})

def productos(request):
	productos = Productos.objects.all()
	return render(request, 'shoponline/productos.html', context={'producto': productos})
