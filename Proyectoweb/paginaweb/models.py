from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombres= models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    numero_identificacion=models.CharField(max_length=15)
    numero_contacto=models.CharField(max_length=15)
    direccion=models.CharField(max_length=50)

    def __str__(self):

        return self.nombres
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.nombre)


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return str(self.nombre)

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre)
    
    
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    etiquetas = models.ManyToManyField(Etiqueta)
    cantidades = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    detalleProducto = models.OneToOneField('DetalleProducto', on_delete=models.CASCADE, related_name='porducto_detalle', null=True)

    def __str__(self):
        return str(self.nombre)
    
class DetalleProducto(models.Model):
    producto = models.OneToOneField(Productos, on_delete=models.CASCADE)
    especificaciones = models.TextField()
    fecha_vencimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"

class Ventas(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta de {self.cantidad} x {self.producto.nombre} a {self.cliente.nombre} el {self.fecha_venta} por {self.total}"
   