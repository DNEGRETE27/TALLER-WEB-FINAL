from django.urls import path
from .views import agregar_clientes,listar_clientes,agregar_productos,listar_productos,registrar_ventas,listar_ventas



urlpatterns = [
    path('agregar_clientes/',agregar_clientes, name='agregar_clientes'),
    path('listar_clientes/',listar_clientes, name='listar_clientes'),
    path('agregar_productos/',agregar_productos, name='agregar_productos'),
    path('listar_productos/',listar_productos, name='listar_productos'),
    path('registrar_ventas/',registrar_ventas, name='registrar_ventas'),
    path('listar_ventas/',listar_ventas, name='listar_ventas'),
    
    
]
