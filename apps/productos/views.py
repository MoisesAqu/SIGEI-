from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm


@login_required
def lista_productos(request):
    productos = Producto.objects.select_related('categoria').all().order_by('nombre')

    total_productos = productos.count()
    en_stock = productos.filter(stock__gt=0).count()
    stock_bajo = productos.filter(stock__gt=0, stock__lte=10).count()
    sin_stock = productos.filter(stock=0).count()

    context = {
        'productos': productos,
        'total_productos': total_productos,
        'en_stock': en_stock,
        'stock_bajo': stock_bajo,
        'sin_stock': sin_stock,
    }

    return render(request, 'productos/lista.html', context)


@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('productos:lista')
    else:
        form = ProductoForm()

    return render(request, 'productos/formulario.html', {
        'form': form,
        'titulo': 'Nuevo Producto'
    })


@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos:lista')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/formulario.html', {
        'form': form,
        'titulo': 'Editar Producto'
    })


@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('productos:lista')

    return render(request, 'productos/eliminar.html', {
        'producto': producto
    })
