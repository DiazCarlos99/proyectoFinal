from django.urls import path, include
from . import views


app_name='empr'

urlpatterns = [

    path('Crear', views.CrearEmpredimiento.as_view(), name="crear_empredimiento"),

    path('Listar', views.ListarEmprendimientos.as_view(), name="listar_emprendimientos"),

    path('Detalle/<int:pk>', views.DetalleEmprendimientos.as_view(), name="detalle_emprendimiento"),

    path('Editar/<int:pk>', views.EditarEmprendimientos.as_view(), name="editar_emprendimientos"),

    path('Eliminar/<int:pk>', views.EliminarEmprendimientos.as_view(), name="eliminar_emprendimiento"),

    path('Filtrar/<str:orden>', views.FiltrarPorOrden.as_view(), name='filtrar_orden'),

    path('Filtrar/<str:nombre>/<str:orden>', views.FiltrarPorOrden.as_view(), name='filtrar_orden_cat'),




]
