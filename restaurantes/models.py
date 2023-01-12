from django.db import models

# Create your models here.
class Restaurantes(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=70)
    especialidad=models.CharField(max_length=20)
    telefono=models.CharField(max_length=11)
    abierto=models.BooleanField()

    def __str__(self):
        return self.nombre
