from django.contrib import admin
from .models import Usuario
from .models import Categoria
from .models import Productos
from .models import Envio
from .models import Orden

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Productos)
admin.site.register(Categoria)
admin.site.register(Envio)
admin.site.register(Orden)
