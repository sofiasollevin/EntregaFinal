from django import forms

class JugadoresFormulario(forms.Form):
    pais= forms.CharField(max_length=30)
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    nacimiento= forms.DateField()
    posicion = forms.CharField(max_length=30)


class ContactosFormulario(forms.Form):
    email= forms.EmailField()
    nombre= forms.CharField(max_length=30)
    contactotelefonico= forms.IntegerField()
    mensaje = forms.CharField(max_length=1000000)
