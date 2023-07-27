from django.urls import path, include
from . import views

app_name='comentarios'

urlpatterns = [
    path('Crear/<int:pk>', views.CrearComentario.as_view(), name='crear_comentario'),
    
    path('Eliminar', views.EliminarComentario.as_view(), name='eliminar_comentario'),
]