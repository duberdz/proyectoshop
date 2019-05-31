#configuracion para las views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('compra/', views.compra, name='compra'),
    path('login/', views.login_required()),
    path('confirm/<string:i>', views.add_product, name='add_product'),
]