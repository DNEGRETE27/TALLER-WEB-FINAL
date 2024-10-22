from django.shortcuts import render, redirect
from .models import Cliente, Productos,Ventas
from .forms import UsuarioForm, ProductosForm, VentasForm
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here
def inicio_web(request):
    return render(request,'inicio_web.html')

def listar_clientes(request):
    clientes= Cliente.objects.all()
    return render(request,'listar_clientes.html',{'clientes': clientes})


def agregar_clientes(request):
    if request.method == 'POST':
        form= UsuarioForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('listar_clientes.html')    

    else:
        form= UsuarioForm(request.POST)
        return render(request,'agregar_clientes.html',{'form': form})    
    


def agregar_productos(request):
    if request.method == 'POST':
        form= ProductosForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('listar_productos.html')    

    else:
        form= ProductosForm(request.POST)
        return render(request,'agregar_productos.html',{'form': form})    
    

def listar_productos(request):
    query = request.GET.get('q')
    productos = Productos.objects.all()
    paginator = Paginator(productos, 8)
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')

    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)

    if precio_min and precio_max:
        productos = productos.filter(precio__gte=precio_min, precio__lte=precio_max)

    if query:
        productos = productos.filter(Q(nombre__icontains=query)| Q(descripcion__icontains=query))


    return render(request, 'listar_productos.html', {'productos': productos})

def registrar_ventas(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            producto = venta.producto           
            if producto.unidades >= venta.cantidad:
                venta.total = producto.precio * venta.cantidad
                producto.cantidad -= venta.cantidad
                producto.save()
                venta.save() 
                return redirect('listar_ventas.html')
            else:
                form.add_error('cantidad', 'No hay suficiente stock .')
    else:
        form = VentasForm()

    return render(request,'registrar_ventas.html', {'form': form})


def listar_ventas(request):
    ventas = Ventas.objects.all().select_related('producto', 'cliente')
    return render(request, 'listar_ventas.html', {'ventas': ventas})