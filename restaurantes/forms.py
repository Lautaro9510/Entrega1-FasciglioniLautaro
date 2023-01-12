from django import forms

class RestaurantesForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    especialidad=forms.CharField(max_length=20)
    direccion= forms.CharField(max_length=70)
    telefono=forms.CharField(max_length=11)
    abierto=forms.BooleanField(required= False)    
   