from django.contrib import admin
from .models import Contactos
# Register your models here.
class ContactosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'mensaje', 'usuario', 'creado')

admin.site.register(Contactos, ContactosAdmin)