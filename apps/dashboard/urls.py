from django.urls import path
from . import views

urlpatterns = [

    path(
        'dashboard/admin/',
        views.dashboard_admin,
        name='dashboard_admin'
    ),

    path(
        'dashboard/compras/',
        views.dashboard_compras,
        name='dashboard_compras'
    ),

    path(
        'dashboard/ventas/',
        views.dashboard_ventas,
        name='dashboard_ventas'
    ),

    path(
        'dashboard/inventario/',
        views.dashboard_inventario,
        name='dashboard_inventario'
    ),
]
