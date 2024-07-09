from django.db import models

class Cliente(models.Model):
    TIPO_OPCIONES = [
    ('particular', 'Particular'),
    ('empresa', 'Empresa')
    ]
    nombre    = models.CharField(max_length=31)
    apellido  = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono  = models.CharField(max_length=20, blank=True, null=True)
    email     = models.EmailField(max_length=255)
    nif       = models.CharField(max_length=12)
    tipo      = models.CharField(max_length=10, choices=TIPO_OPCIONES, default='particular')

    def __str__(self) -> str:
        return f"{self.nombre}, {self.nif}"

class Factura(models.Model):
    importe   = models.DecimalField(decimal_places=2, max_digits=8)
    impuestos = models.IntegerField(default=21) # %
    cliente   = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    created_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Factura #{self.id} - {self.cliente.nombre} {self.cliente.apellido}"
    
    class Meta:
        verbose_name_plural = "Facturas"