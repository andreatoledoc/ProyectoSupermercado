from django.shortcuts import render
from AppAdministracion.models import Articulo
from django.http import HttpResponse

# Create your views here.

def articulos (request):
    return render (request, 'articulos.html')

def inicio (request):
    return render(request, "AppAdminsitracion/inicio.html")

def proveedores (request):
    return HttpResponse ('Vista de proveedores')

def clientes (request):
    return HttpResponse ('Vista de clientes')

def empleados (request):
    return HttpResponse ('Vista de empleados')



