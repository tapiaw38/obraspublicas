from django.db import models
from usuario.models import Usuario
from proyectista.models import Proyectista
# Create your models here.


class Plano(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    proyectista = models.ForeignKey(Proyectista, null=False, blank=False, on_delete=models.CASCADE)
    dir_obra = models.CharField(max_length=50)
    precio_metro = models.IntegerField()
    metros = models.IntegerField()
    total = models.FloatField(editable=False)
    cuota = models.IntegerField()
    deuda = models.FloatField(editable=False)
    pago = models.FloatField(default=0)
    fecha_pago = models.DateField(null=True, blank= True)
    pago2 = models.FloatField(default=0)
    fecha_pago2 = models.DateField(null=True, blank= True)
    pago3 = models.FloatField(default=0)
    fecha_pago3 = models.DateField(null=True, blank= True)
    pago4 = models.FloatField(default=0)
    fecha_pago4 = models.DateField(null=True, blank= True)
    valor_cuota = models.FloatField(editable=False)
    s_cuota1 = models.FloatField(editable=False)
    s_cuota2 = models.FloatField(editable=False)
    s_cuota3 = models.FloatField(editable=False)
    s_cuota4 = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        self.total = self.precio_metro*self.metros
        self.deuda = self.total - self.pago -self.pago2 -self.pago3 -self.pago4
        if self.cuota == 1:
            self.valor_cuota = self.total / 1
        elif self.cuota == 2:
            self.valor_cuota = self.total / 2
        elif self.cuota == 3:
            self.valor_cuota = self.total / 3
        elif self.cuota == 4:
            self.valor_cuota = self.total / 4
        self.s_cuota1 = self.total - self.valor_cuota
        self.s_cuota2 = self.total - 2 * self.valor_cuota
        self.s_cuota3 = self.total - 3 * self.valor_cuota
        self.s_cuota4 = self.total - 4 * self.valor_cuota
        if self.deuda < 0:
            return '¡Lo abonado es mayor a la cuota a pagar!'


        super(Plano,self).save( *args, **kwargs)

