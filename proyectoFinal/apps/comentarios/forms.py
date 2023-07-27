from django import forms
from .models import Comentarios

class Form_Alta(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('texto',)