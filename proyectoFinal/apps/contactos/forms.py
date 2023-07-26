from django import forms
from .models import Contactos


class Form_Alta(forms.ModelForm):

    class Meta:
        model = Contactos
        fields = ('nombre', 'email', 'asunto', 'mensaje')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('debe ingresar un correo valido.')
        return email