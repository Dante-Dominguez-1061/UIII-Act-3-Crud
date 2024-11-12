from django.db import models

# Create your models here.

class Consola(models.Model):
    id_consola = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    precio = models.PositiveSmallIntegerField()
    fecha_lanzamiento = models.DateField()
    compañia = models.CharField(max_length=100)
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre