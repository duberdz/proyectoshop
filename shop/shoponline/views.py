from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required


def login(request):
	return render(request, 'shoponline/login.html', {})


def productos(request):
	productos = Productos.objects.all()
	return render(request, 'shoponline/productos.html', context={'producto': productos})

def compra(request):
	compra = Orden.objects.all()
	return render(request, 'shoponline/compra.html', context={'compra':compra})