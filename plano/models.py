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
    cuota = models.BooleanField(default=False)
    pago = models.IntegerField(default=0)
    pago2 = models.IntegerField(default=0)
    fecha_pago2 = models.DateField(null=True, blank= True)
    pago3 = models.IntegerField(default=0)
    fecha_pago3 = models.DateField(null=True, blank= True)
    fecha_pago = models.DateField(null=True, blank= True)
    deuda = models.PositiveIntegerField(editable=False)
    valor_cuota = models.PositiveIntegerField(editable=False)
    s_cuota1 = models.PositiveIntegerField(editable=False)
    s_cuota2 =  models.PositiveIntegerField(editable=False)
    s_cuota3 = models.PositiveIntegerField(editable=False)

    def save(self, *args, **kwargs):
        self.total = self.precio_metro*self.metros
        self.deuda = self.total - self.pago -self.pago2 -self.pago3
        self.valor_cuota = self.total/3
        self.s_cuota1 = self.total - self.valor_cuota
        self.s_cuota2 = self.total - 2*self.valor_cuota
        self.s_cuota3 = self.total - 3* self.valor_cuota
        if self.deuda < 0:
            return '¡Lo abonado es mayor a la cuota a pagar!'
        super(Plano,self).save( *args, **kwargs)

