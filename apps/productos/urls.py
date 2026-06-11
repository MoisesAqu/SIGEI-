from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('productos/', views.lista_productos, name='lista'),
    path('productos/crear/', views.crear_producto, name='crear'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar'),
]
