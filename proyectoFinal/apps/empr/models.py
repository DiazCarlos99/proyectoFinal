from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to='categorias')
    resumen = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class Emprendimientos(models.Model):
    creado = models.DateTimeField(
		'creado',
		auto_now_add=True
	)
    modificado = models.DateTimeField(
		'modificado', 
		auto_now=True
	)
    titulo = models.CharField(max_length=80)
    resumen = models.TextField()
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to= 'empr')
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    
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
    
    def MisComentarios(self):
        return self.comentarios_set.all()

        
    def __str__(self):
        return self.titulo