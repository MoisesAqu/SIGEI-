from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_admin(request):
    return render(request, 'dashboard/admin.html')


@login_required
def dashboard_compras(request):
    return render(request, 'dashboard/compras.html')


@login_required
def dashboard_ventas(request):
    return render(request, 'dashboard/ventas.html')


@login_required
def dashboard_inventario(request):
    return render(request, 'dashboard/inventario.html')
    