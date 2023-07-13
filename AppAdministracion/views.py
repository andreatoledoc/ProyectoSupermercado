from django.shortcuts import render
from AppAdministracion.models import Articulo, Cliente, Empleado, Proveedor
from django.http import HttpResponse
from AppAdministracion.forms import ArticuloFormulario, ClienteFormulario, EmpleadoFormulario, ProveedorFormulario

# Create your views here.

'''
def articulos (request):
    return render (request, 'AppAdministracion/articulos.html')
'''

def inicio (request):
    return render(request, "AppAdministracion/inicio.html")

def proveedores (request):
    return render(request, "AppAdministracion/proveedores.html")

def clientes (request):
    return render(request, "AppAdministracion/clientes.html")

def empleados (request):
    return render(request, "AppAdministracion/empleados.html")

#Vista de formularios

def articulos (request):
    if request.method == "POST":
        miFormulario = ArticuloFormulario(request.POST) #Donde llega la información del html
        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data #Limpiamos la forma en que recibimos la información
            articulo = Articulo(nombre = informacion['nombre'], 
                                codigo = informacion['codigo'], 
                                categoria = informacion['categoria'])
            articulo.save()
        return render (request, 'AppAdministracion/inicio.html')
    
    else:
        miFormulario = ArticuloFormulario()

    return render (request, 'AppAdministracion/articulos.html', {"miFormulario": miFormulario})


def clienteFormulario (request):
    if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST) #Donde llega la información del html
        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data #Limpiamos la forma en que recibimos la información
            cliente = Cliente(nombre = informacion['nombre'], 
                               telefono = informacion['telefono'])
            cliente.save()
        return render (request, 'AppAdministracion/inicio.html')
    
    else:
        miFormulario = ClienteFormulario()

    return render (request, 'AppAdministracion/clienteFormulario.html', {"miFormulario": miFormulario})


def empleadoFormulario (request):
    if request.method == "POST":
        miFormulario = EmpleadoFormulario(request.POST) #Donde llega la información del html
        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data #Limpiamos la forma en que recibimos la información
            empleado = Empleado(nombre = informacion['nombre'], 
                               direccion = informacion['direccion'], 
                               email = informacion ['email'], 
                               telefono = informacion ['telefono'],
                               puesto = informacion ['puesto'])
            empleado.save()
        return render (request, 'AppAdministracion/inicio.html')
    
    else:
        miFormulario = EmpleadoFormulario()

    return render (request, 'AppAdministracion/empleadoFormulario.html', {"miFormulario": miFormulario})


def proveedorFormulario (request):
    if request.method == "POST":
        miFormulario = ProveedorFormulario(request.POST) #Donde llega la información del html
        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data #Limpiamos la forma en que recibimos la información
            proveedorFormulario = Proveedor(nombre = informacion['nombre'], 
                               direccion = informacion['direccion'], 
                               email = informacion ['email'], 
                               telefono = informacion ['telefono'])
            proveedorFormulario.save()
        return render (request, 'AppAdministracion/inicio.html')
    
    else:
        miFormulario = ProveedorFormulario()

    return render (request, 'AppAdministracion/proveedorFormulario.html', {"miFormulario": miFormulario})


def busquedaCategoria(request):
    return render (request , 'AppAdministracion/busquedaCategoria.html')

def buscar (request):

    if request.GET['categoria']:
        #respuesta = f"Estoy buscando la categoria: {request.GET['categoria']}"
        categoria = request.GET['categoria']
        articulos = Articulo.objects.filter(categoria__icontains = categoria)
        return render (request, 'AppAdministracion/inicio.html', {'articulos': articulos, 'categoria':categoria})
    else:
        respuesta = "No enviaste datos"
    return render (request, 'AppAdministracion/inicio.html', {'respuesta': respuesta})