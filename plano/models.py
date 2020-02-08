from django.db import models
from usuario.models import Usuario
# Create your models here.

class Plano(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    dir_obra = models.CharField(max_length=50)
    precio_metro = models.IntegerField()
    metros = models.IntegerField()
    total = models.IntegerField(editable=False)
    pago = models.IntegerField(default=0)
    pago2 = models.IntegerField(default=0)
    fecha_pago2 = models.DateField(null=True, blank= True)
    pago3 = models.IntegerField(default=0)
    fecha_pago3 = models.DateField(null=True, blank= True)
    fecha_pago = models.DateField(null=True, blank= True)
    deuda = models.PositiveIntegerField(editable=False)

    def save(self, *args, **kwargs):
        self.total = self.precio_metro*self.metros
        self.deuda = self.total - self.pago -self.pago2 -self.pago3
        super(Plano,self).save( *args, **kwargs)

