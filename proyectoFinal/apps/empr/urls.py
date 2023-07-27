from django.urls import path, include
from . import views


app_name='empr'

urlpatterns = [
    
    path('Crear', views.CrearEmpredimiento.as_view(), name="crear_empredimiento"),
    
    path('Listar', views.ListarEmprendimientos.as_view(), name="listar_emprendimientos"),
    
    path('Detalle/<int:pk>', views.DetalleEmprendimientos.as_view(), name="detalle_emprendimiento"),
     
    path('Editar/<int:pk>', views.EditarEmprendimientos.as_view(), name="editar_emprendimientos"),
    
    path('Eliminar/<int:pk>', views.EliminarEmprendimientos.as_view(), name="eliminar_emprendimiento"),
    
    path('Filtrar/<str:nombre>', views.FiltrarEmprendimientos.as_view(), name="filtrar_emprendimientos"),
    
    #path('Filtrar/categorias/', views.Categorias.as_view(), name="emprendimientos_categorias"),
    
    path('Filtrar/antiguedad/<str:orden>/', views.FiltrarPorAntiguedad.as_view(), name='emprendimiento_antiguedad'),
    
    path('Filtrar/alfabetico/<str:orden>/', views.FiltrarPorOrdenAlfabetico.as_view(), name='emprendimiento_alfabetico'),
     
    
] 
