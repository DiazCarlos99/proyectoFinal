from django.shortcuts import render
from .models import Contactos

from django.views.generic import CreateView
from django.urls import reverse_lazy
#CONTROLA SI EL USUARIO ESTA LOGEADO
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Form_Alta
#se importan los alert o mensajes
from django.contrib import messages
# enviar correo
from django.core.mail import send_mail
class PrimerContacto(LoginRequiredMixin, CreateView):
    model = Contactos
    form_class = Form_Alta
    template_name = 'contactos/contacto.html'
    success_url = reverse_lazy('contactos:contacto') 
    
    def form_valid(self, form):
        if form.is_valid():    
            form.instance.usuario = self.request.user
            # guardar el formulario
            contacto = form.save()

            #enviar correo
            subject = 'Confirmación de contacto'
            message = 'HEMOS RECIBIDO SU MENSAJE CON ÉXITO. MUY PRONTO NOS PONDREMOS EN CONTACTO CON USTED.'
            from_email = 'tu_correo_electronico'
            recipient_list = [contacto.email]

            send_email = [subject, message, from_email, recipient_list]


            # si da ok. se envia el siguiente mensaje
            messages.success(self.request, 'Se ha enviado el mensaje con exito.')
            return super().form_valid(form)
        else:
            # Si el formulario no es válido, volver a mostrarlo con los errores
            return self.form_invalid(form) 