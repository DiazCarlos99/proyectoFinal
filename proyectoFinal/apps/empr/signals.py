from django.apps import AppConfig
import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Emprendimientos

class EmprendimientosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.empr'
    
    def ready(self):
        import apps.empr.signals
        


@receiver(pre_delete, sender=Emprendimientos)
def eliminar_imagenes_emprendimiento(sender, instance, **kwargs):
    if instance.imagen:
        ruta_imagen = instance.imagen.path

        if os.path.isfile(ruta_imagen):
            os.remove(ruta_imagen)