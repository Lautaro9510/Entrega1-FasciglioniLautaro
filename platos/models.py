from django.db import models

# Create your models here.
class Platos(models.Model):
    nombre=models.CharField(max_length=50)
    especialidad=models.CharField(max_length=20)
    apto_vegano=models.BooleanField()
    apto_vegetariano=models.BooleanField()
    apto_celiaco=models.BooleanField()
    stock=models.BooleanField()
    precio=models.FloatField()

    def __str__(self):
        return self.nombre    
