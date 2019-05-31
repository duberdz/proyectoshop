from django.contrib.auth import authenticate
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request, 'home.html', {})

def login(request):
	form = AuthenticationForm()
	return render(request = request,template_name='old_login.html',context={"form":form})

@login_required(login_url='/accounts/login')
def add_product(nombre):
	context = {}
	articulo = Carrito.objects()
	articulo.producto = nombre
	articulo.usuario = form.cleaned_data.get('username')
	articulo.pago = 'pendiente'
	articulo.save()
		#return HttpResponseRedirect('confirm.html')
	return render_to_response('confirm.html')

def confirm(request):
	return render(request, 'confirm.html', {})

@login_required(login_url='/accounts/login')
def compra(request):
	cart = Carrito.objects.all()
	cart = cart.filter(user=request.user)
	return render(request, 'compra.html', context={'cart': cart})

@login_required(login_url='/accounts/login')
def productos(request):
	all_productos = Productos.objects.all()
	return render(request, 'productos.html', context={'all_productos': all_productos})

def compra(request):
	compra = Carrito.objects.all()
	return render(request, 'compra.html', context={'compra':compra})

def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('/')
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Invalid username or password")

	form = AuthenticationForm()
	return render(request = request, template_name='old_login.html', context={"form":form})