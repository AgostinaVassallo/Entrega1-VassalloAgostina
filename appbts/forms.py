from django import forms

class BtsForm (forms.Form):
    integrantes = forms.CharField(label="Integrantes", max_length=50)
#    nacimiento= forms.DateField(label='Fecha de nacimiento') #etiqueta
