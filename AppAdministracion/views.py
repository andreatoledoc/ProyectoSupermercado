from django.shortcuts import render
from AppAdministracion.models import Articulo
from django.http import HttpResponse

# Create your views here.

def articulos (request):
    return render (request, 'AppAdministracion/articulos.html')

def inicio (request):
    return render(request, "AppAdministracion/inicio.html")

def proveedores (request):
    return render(request, "AppAdministracion/proveedores.html")

def clientes (request):
    return render(request, "AppAdministracion/clientes.html")

def empleados (request):
    return render(request, "AppAdministracion/empleados.html")



