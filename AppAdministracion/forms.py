from django import forms

class ClienteFormulario (forms.Form):
    nombre = forms.CharField()
    telefono = forms.IntegerField()

class ProveedorFormulario (forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField ()
    email = forms.EmailField ()
    telefono = forms.IntegerField()

class ArticuloFormulario (forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()
    categoria = forms.CharField()

class EmpleadoFormulario (forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField ()
    email = forms.EmailField ()
    telefono = forms.IntegerField()
    puesto = forms.CharField()

