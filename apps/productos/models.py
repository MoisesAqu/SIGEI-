from django.db import models
from apps.categorias.models import Categoria


class Producto(models.Model):

    UNIDADES_MEDIDA = [
        ('unidad', 'Unidad'),
        ('metro', 'Metro'),
        ('kg', 'Kilogramo'),
        ('litro', 'Litro'),
        ('paquete', 'Paquete'),
        ('caja', 'Caja'),
        ('rollo', 'Rollo'),
        ('bolsa', 'Bolsa'),
    ]

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT
    )

    nombre = models.CharField(max_length=150)

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    sku = models.CharField(
        max_length=30,
        unique=True
    )

    marca = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    unidad_medida = models.CharField(
        max_length=20,
        choices=UNIDADES_MEDIDA,
        default='unidad'
    )

    ubicacion_almacen = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    imagen = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True
    )

    precio_compra = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    precio_venta = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.IntegerField(default=0)

    stock_minimo = models.IntegerField(default=0)

    activo = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre