from django import forms

class RepartidoresForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    direccion= forms.CharField(max_length=70)
    telefono=forms.CharField(max_length=11)
    email=forms.EmailField()
    vehiculo=forms.CharField(max_length=20)   
    esta_trabajando=forms.BooleanField()
