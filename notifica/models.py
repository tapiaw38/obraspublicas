from django.db import models
from usuario.models import Usuario
import datetime
# Create your models here.

class Notifica(models.Model):
    fecha = models.DateTimeField(help_text='01/01/2020 09:00')
    lugar = models.CharField(max_length=60)
    caracteristicas = models.CharField(max_length=60)
    usuario = models.ForeignKey(Usuario,null=False, blank=False, on_delete=models.CASCADE)
    hechos = models.CharField(max_length=200)
    situacion = models.NullBooleanField(default=False)
    fecha_limite = models.DateTimeField(null=True, blank=True)
    fecha_presenta = models.DateField(null=True, blank=True)




