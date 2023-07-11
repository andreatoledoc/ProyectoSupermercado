from django.shortcuts import render
from AppAdministracion.models import Articulo
from django.http import HttpResponse

# Create your views here.

def articulo (self):
    articulo = Articulo (nombre = "Galletas", codigo ='21111', categoria = "Alimentacion" )
    articulo.save ()

    documentoDeTexto = f'---> Articulo: {articulo.nombre} Codigo: {articulo.codigo} Categoria: {articulo.categoria}'

    return HttpResponse(documentoDeTexto)

