from django.contrib.auth import authenticate
from django.core.checks import messages
from django.shortcuts import render, redirect
#from .forms import NewUserForm
#from django.http import HttpResponse

# Create your views here.
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request, 'home.html', {})

def login(request):
	form = AuthenticationForm()
	return render(request = request,template_name='login.html',context={"form":form})

def productos(request):
	productos = Productos.objects.all()
	return render(request, 'productos.html', context={'producto': productos})

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
	return render(request = request, template_name='login.html', context={"form":form})