from django.db import models

# Create your models here.

class Cliente (models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()

class Proveedor (models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField (max_length=50)
    email = models.EmailField ()
    telefono = models.IntegerField()

class Articulo (models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()
    categoria = models.CharField(max_length=40)

class Empleado (models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField (max_length=50)
    email = models.EmailField ()
    telefono = models.IntegerField()
    puesto = models.CharField(max_length=40)




