from django.urls import path
from . import views

app_name="users"

urlpatterns = [

    path('users', views.Users, name = 'users'),

    path('Registro', views.Registro.as_view(), name="registrar"),

]