from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    direccion = models.CharField(max_length=50, verbose_name='dirección')
    catastro = models.CharField(max_length=50)
    tel = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.dni)