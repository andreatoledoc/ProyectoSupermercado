from django.shortcuts import render
from AppAdministracion.models import Articulo
from django.http import HttpResponse

# Create your views here.

def articulos (self):
    articulos = Articulo (nombre = "Galletas", codigo ='21111', categoria = "Alimentacion" )
    articulos.save ()

    documentoDeTexto = f' Articulo: {articulos.nombre} Codigo: {articulos.codigo} Categoria: {articulos.categoria}'

    return HttpResponse(documentoDeTexto)

def inicio (request):
    return HttpResponse ('Vista de Inicio')

def proveedores (request):
    return HttpResponse ('Vista de proveedores')

def clientes (request):
    return HttpResponse ('Vista de clientes')

def empleados (request):
    return HttpResponse ('Vista de empleados')



