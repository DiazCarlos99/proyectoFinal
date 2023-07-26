from django.db import models
from django.contrib.auth.models import User

class Contactos(models.Model):
	creado = models.DateTimeField(
			'creado',
			auto_now=True
		)

	nombre = models.CharField(max_length=80)
	email = models.CharField(max_length=80)
	asunto = models.CharField(max_length=120)
	mensaje = models.TextField()
	estado = models.BooleanField(default=False)
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
	        return f"Mensaje de {self.nombre} - {self.asunto}" 