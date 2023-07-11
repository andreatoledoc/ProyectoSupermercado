from django.urls import path, include
from AppAdministracion import views

urlpatterns = [
    path ('', views.inicio),
    path ('clientes', views.clientes, name = 'Clientes'),
    path ('proveedores', views.proveedores, name = 'Proveedores'),
    path ('articulos', views.articulos, name = 'Articulos'),
    path ('empleados', views.empleados, name = 'Empleados'),
]

