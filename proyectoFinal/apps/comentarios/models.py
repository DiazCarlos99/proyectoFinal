from django.db import models
from django.contrib.auth.models import User
from apps.empr.models import Emprendimientos
from django.utils import timezone
from datetime import timedelta
# Create your models here.

class Comentarios(models.Model):
    creado = models.DateTimeField(
        'creado',
        auto_now_add=True
    )
    
    modificado = models.DateTimeField(
        'modificado',
        auto_now=True
    )
    
    texto = models.TextField(max_length = 1000)
    estado = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    emprendimiento = models.ForeignKey(Emprendimientos, on_delete = models.CASCADE)
    
    def get_creado_naturaltime(self):
        now = timezone.now()
        diff = now - self.creado
        
        if diff < timedelta(minutes=1):
            return 'hace unos segundos'
        elif diff < timedelta(hours=1):
            minutes = diff.seconds // 60
            return f'hace {minutes} minutos'
        elif diff < timedelta(days=1):
            hours = diff.seconds // 3600
            return f'hace {hours} horas'
        elif diff < timedelta(days=30):
            days = diff.days
            return f'hace {days} días'
        else:
            return self.creado.strftime('%d de %B de %Y a las %H:%M')
        
    def get_modificado_naturaltime(self):
        now = timezone.now()
        diff = now - self.modificado
        print(diff)
        
        if diff < timedelta(minutes=1):
            return 'hace unos segundos'
        elif diff < timedelta(hours=1):
            minutes = diff.seconds // 60
            return f'hace {minutes} minutos'
        elif diff < timedelta(days=1):
            hours = diff.seconds // 3600
            return f'hace {hours} horas'
        elif diff < timedelta(days=30):
            days = diff.days
            return f'hace {days} días'
        else:
            return self.creado.strftime('%d de %B de %Y a las %H:%M')
    
    def __str__(self):
        return self.texto
    
    def save(self, *args, **kwargs):
        print("Guardando comentario...")
        super(Comentarios, self).save(*args, **kwargs)