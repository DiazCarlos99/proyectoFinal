from django import forms
from .models import Contactos


class Form_Alta(forms.ModelForm):

    class Meta:
        model = Contactos
        fields = ('nombre', 'email', 'asunto', 'mensaje')