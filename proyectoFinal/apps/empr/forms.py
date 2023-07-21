from django import forms
from .models import Emprendimientos


class Form_Alta(forms.ModelForm):

    class Meta:
        model = Emprendimientos
        fields = ('titulo','contenido','imagen','categoria', 'resumen')

class Form_Modificacion(forms.ModelForm):

    class Meta:
        model = Emprendimientos
        fields = ('contenido','imagen','categoria', 'resumen', 'imagen')