from django import forms

class PlatosForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    especialidad=forms.CharField(max_length=20)
    apto_vegano=forms.BooleanField(required= False)
    apto_vegetariano=forms.BooleanField(required= False)
    apto_celiaco=forms.BooleanField(required= False)
    stock=forms.BooleanField(required= False)
    precio=forms.FloatField()