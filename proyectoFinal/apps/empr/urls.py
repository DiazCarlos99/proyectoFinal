from django.urls import path, include
from . import views

app_name='empr'

urlpatterns = [
    path('Crear', views.CrearEmpredimiento.as_view(), name="crear_empredimiento"),
    
    path('Listar', views.ListarEmprendimientos.as_view(), name="listar_emprendimientos"),
    
    path('Detalle/<int:pk>', views.DetalleEmprendimientos, name="detalle_emprendimiento"),
     
     
] 