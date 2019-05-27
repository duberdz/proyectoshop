from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.nombre)

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    categoria = models.ForeignKey('Categoria' , on_delete=models.SET_NULL , null=True)

    def __str__(self):
         return 'Productos :' + self.nombre

class Carrito(models.Model):
    usuario = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    producto = models.ForeignKey('Productos', on_delete=models.SET_NULL, null=True)
    pago = models.CharField(max_length=10)
