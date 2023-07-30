from django.shortcuts import render
from .models import Contactos

from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Form_Alta

from django.contrib import messages

from django.core.mail import send_mail
class PrimerContacto(LoginRequiredMixin, CreateView):
    model = Contactos
    form_class = Form_Alta
    template_name = 'contactos/contacto.html'
    success_url = reverse_lazy('contactos:contacto') 
    
    def form_valid(self, form):
        if form.is_valid():    
            form.instance.usuario = self.request.user
            contacto = form.save()
            subject = 'Confirmación de contacto'
            message = 'HEMOS RECIBIDO SU MENSAJE CON ÉXITO. MUY PRONTO NOS PONDREMOS EN CONTACTO CON USTED.'
            from_email = 'tu_correo_electronico'
            recipient_list = [contacto.email]

            send_email = [subject, message, from_email, recipient_list]
            messages.success(self.request, 'Se ha enviado el mensaje con exito.')
            return super().form_valid(form)
        else:
            return self.form_invalid(form) 