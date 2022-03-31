from django import forms
from django.forms import ModelForm
from blog.models import Posteos, Suscriptores, Contacto


class FormularioPosteos(forms.ModelForm):
        class Meta:
                model = Posteos
                fields = "__all__"
                widgets = {"Fecha": forms.DateInput(attrs={'type': 'date'})}

        titulo = forms.CharField(max_length=60)
        texto = forms.CharField(max_length=280)

class Suscribirse(forms.ModelForm):

        class Meta:
                model = Suscriptores
                fields = "__all__"

        nombre = forms.CharField(max_length=60)
        apellido = forms.CharField (max_length=60)
        mail = forms.EmailField()

class FormularioContacto(forms.ModelForm):

        class Meta:
                model = Contacto
                fields = "__all__"

        nombre = forms.CharField(max_length=60)
        apellido = forms.CharField (max_length=60)
        mail = forms.EmailField()
        texto = forms.CharField()