from django.db import models
from usuario.models import Usuario
# Create your models here.

class Plano(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    dir_obra = models.CharField(max_length=50, verbose_name='direccion de la obra')
    precio_metro = models.IntegerField(verbose_name='precio por metro cuadrado')
    metros = models.IntegerChoices()
    total = models.IntegerField(default=precio_metro*metros, null=True, blank=True)
    pago = models.IntegerField(default=0,null=True, blank=True)
    fecha_pago = models.DateField(null=True, blank= True)
    deuda = models.IntegerField(default=total-pago, null=True, blank=True)