from django.db import models

class Cliente(models.Model):
    TIPO_OPCIONES = [
    ('particular', 'Particular'),
    ('empresa', 'Empresa')
    ]
    nombre    = models.CharField(max_length=31)
    apellido  = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono  = models.CharField(max_length=12, blank=True, null=True)
    emial     = models.EmailField(max_length=255)
    nif       = models.CharField(max_length=12)
    tipo      = models.CharField(max_length=10, choices=TIPO_OPCIONES, default='particular')

class Factura(models.Model):
    importe   = models.DecimalField(decimal_places=2, max_digits=8)
    impuestos = models.IntegerField(default=21) # %
    cliente   = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    created_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)