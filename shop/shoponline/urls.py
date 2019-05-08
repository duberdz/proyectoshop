#configuracion para las views
from django.urls import path
#from shop.shoponline import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]