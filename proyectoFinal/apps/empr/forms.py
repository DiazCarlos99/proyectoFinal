from django import forms
from .models import Emprendimientos


class Form_Alta(forms.ModelForm):

    class Meta:
        model = Emprendimientos
        fields = ('titulo','resumen','contenido','categoria','imagen' )
        labels = {
            'resumen': 'Breve Descripción',
            'contenido': 'Descripción',
        }
class Form_Modificacion(forms.ModelForm):

    class Meta:
        model = Emprendimientos
        fields = ('titulo','resumen','contenido','categoria','imagen')
        labels = {
            'resumen': 'Breve Descripción',
            'contenido': 'Descripción',
        }