from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)

    def __str__(self):
        return 'Usuario :' + self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return 'Categoria :' + self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    categoria = models.ForeignKey('Categoria' , on_delete=models.SET_NULL , null=True)

    def __str__(self):
         return 'Productos :' + self.nombre

class Envio(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()

    def __str__(self):
         return 'Envio :' + self.nombre

class Orden(models.Model):
    usuario = models.ForeignKey('Usuario' , on_delete=models.SET_NULL , null=True)
    producto = models.ForeignKey('Productos' , on_delete=models.SET_NULL , null=True)
    envio = models.ForeignKey('Envio' , on_delete=models.SET_NULL , null=True)
