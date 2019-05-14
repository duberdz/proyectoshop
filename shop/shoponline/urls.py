#configuracion para las views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('productos/', views.productos, name='productos'),
    path('compra/', views.compra, name='compra'),
]