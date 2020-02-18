from django.db import models
from usuario.models import Usuario
# Create your models here.

class Obra(models.Model):
    fecha = models.DateTimeField(help_text='01/01/2020 09:00')
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    ubicacion_obra = models.CharField(max_length=100)
    dias = models.IntegerField()
    presentacion = models.NullBooleanField(default=False)
    fecha_limite = models.DateTimeField(null=True, blank=True)
    fecha_presenta = models.DateField(null=True, blank=True)