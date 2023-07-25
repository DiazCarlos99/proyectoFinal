from django.urls import path, include
from . import views

app_name='contactos'

urlpatterns = [
    
    path('', views.PrimerContacto.as_view(), name="contacto"),
]
 