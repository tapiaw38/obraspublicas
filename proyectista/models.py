from django.db import models

# Create your models here.
class Proyectista(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    direccion = models.CharField(max_length=50, verbose_name='dirección')
    profesion = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    tel = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.profesion, self.nombre)
