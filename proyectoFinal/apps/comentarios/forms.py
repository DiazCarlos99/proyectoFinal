from django import forms
from .models import Comentarios

class Form_Modificacion(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('texto',)