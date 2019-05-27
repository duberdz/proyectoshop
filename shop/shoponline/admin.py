from django.contrib import admin
from .models import Categoria
from .models import Productos
from .models import Carrito

# Register your models here.

admin.site.register(Productos)
admin.site.register(Categoria)
admin.site.register(Carrito)
