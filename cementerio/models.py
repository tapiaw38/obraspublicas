from django.db import models
from usuario.models import Usuario
# Create your models here.
class Cementerio(models.Model):
    # Compra de lotes
    fecha_compra = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    construccion = models.CharField(max_length=50)# Nicho, Mansuleo, Fosa
    lote = models.IntegerField()
    lote_num = models.CharField(max_length=30)
    lote_cuadro = models.CharField(max_length=30)
    dimension = models.CharField(max_length=30)
    precio_lote = models.FloatField()
    vigencia = models.IntegerField() # Años de vigencia del contrato
    caduca = models.DateTimeField(null=True, blank=True) # Fecha de vencimiento del contrato
    dias_concesion = models.IntegerField(default=30) # Dias para renovacion de contratos
    caduca_concesion = models.DateTimeField(null=True, blank=True) # Fecha de vencimiento total
    # Al iniciar los trabajos
    #trabajo_inicio = models.NullBooleanField(default=False) # Inicio del trabajo
    prorroga_iniciar = models.IntegerField(default=180)
    fin_prorroga_iniciar = models.DateTimeField(null=True, blank=True)
    # al sacar permisos

    fecha_inicio = models.DateTimeField(null=True, blank=True)  # fecha de inicio
    prorroga_trabajo = models.IntegerField(default=240) # prorroga para finalizar despues de haber sacado permiso
    fecha_final = models.DateTimeField(null=True, blank=True)  # Fin prorroga

    trabajo_final = models.NullBooleanField(default=False) # Finalizar trabajo
    trabajo_final_fecha = models.DateTimeField(null=True, blank=True) # Fecha finalizacion (antes o despues)

    #deudas
    deuda_anual1 = models.FloatField(default=0)
    deuda_anual2 = models.FloatField(default=0)
    deuda_anual3 = models.FloatField(default=0)
    deuda_anual4 = models.FloatField(default=0)
    deuda_total = models.FloatField(editable=False)
    # Abono anual
    abono_anual = models.FloatField() # Abono mensual
    #fechas de pagos anuales
    fecha_anual1 = models.DateTimeField(null=True, blank=True) # Fecha de pago de mensualidad
    monto_anual1 = models.FloatField(default=0)

    fecha_anual2 = models.DateTimeField(null=True, blank=True) # Fecha de pago de mensualidad
    monto_anual2 = models.FloatField(default=0)

    fecha_anual3 = models.DateTimeField(null=True, blank=True) # Fecha de pago de mensualidad
    monto_anual3 = models.FloatField(default=0)

    fecha_anual4 = models.DateTimeField(null=True, blank=True) # Fecha de pago de mensualidad
    monto_anual4 = models.FloatField(default=0)

    contrato = models.ImageField(null=True,blank=True) # imagen del contrato
    # Permisos de construccion
    metro = models.FloatField(default=0)
    precio_metro = models.FloatField(default=0)
    total = models.FloatField(editable=False)
    plano = models.NullBooleanField(default=False)

    def save(self, *args, **kwargs):
        self.total=self.metro+self.precio_metro
        # Montos de pagos anuales
        if self.vigencia == 1:
            self.deuda_anual1 = self.abono_anual
        elif self.vigencia == 2:
            self.deuda_anual1 = self.abono_anual
            self.deuda_anual2 = self.abono_anual
        elif self.vigencia == 3:
            self.deuda_anual1 = self.abono_anual
            self.deuda_anual2 = self.abono_anual
            self.deuda_anual3 = self.abono_anual
        elif self.vigencia == 4:
            self.deuda_anual1 = self.abono_anual
            self.deuda_anual2 = self.abono_anual
            self.deuda_anual3 = self.abono_anual
            self.deuda_anual4 = self.abono_anual
        # Monto total
        self.deuda_total = self.deuda_anual1+self.deuda_anual2+self.deuda_anual3+self.deuda_anual4
        super(Cementerio, self).save(*args, **kwargs)


