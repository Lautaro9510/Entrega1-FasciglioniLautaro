from django.db import models

# Create your models here.
class Repartidores(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=70)
    email=models.EmailField()
    telefono=models.CharField(max_length=11)
    vehiculo=models.CharField(max_length=20)
    esta_trabajando=models.BooleanField(default=True)
    def __str__(self):
        return self.nombre