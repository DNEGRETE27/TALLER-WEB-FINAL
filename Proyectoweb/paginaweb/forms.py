from django import forms
from .models import Cliente, Productos, Ventas


class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['nombres','apellidos','numero_identificacion','numero_contacto','direccion']
    

class ProductosForm(forms.ModelForm):
    class Meta:
        model=Productos
        fields=['nombre','categoria','proveedor','etiquetas','cantidades','precio','descripcion','detalleProducto']

class VentasForm(forms.ModelForm):
    class Meta:
        model= Ventas
        fields=['producto','cliente','cantidad']   