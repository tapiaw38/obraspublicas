from django.db import models
from usuario.models import Usuario
# Create your models here.

class Plano(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    dir_obra = models.CharField(max_length=50, verbose_name='direccion de la obra')
    precio_metro = models.IntegerField(default=0,verbose_name='precio por metro cuadrado')
    metros = models.IntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    pago = models.IntegerField(default=0)
    fecha_pago = models.DateField(null=True, blank= True)
    deuda = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args,**kwargs):
        total=self.metros*self.precio_metro
        deuda=self.total-self.pago
        super(Plano,self).save(*args,**kwargs)

