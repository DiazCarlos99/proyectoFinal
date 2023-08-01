"""
URL configuration for proyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Home, name = 'home'),

    path('sobre_nosotros', views.Sobre_nosotros, name = 'sobre_nosotros'),

    path('contacto', views.Contacto, name = 'contacto'),



    #URLS DE AUTH
    path('login/',auth.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth.LogoutView.as_view(),name="logout"),

    #urls de usuarios
    path('usuarios/', include('apps.usuarios.urls')),

    # url de de las aplicaciones

    #url de empr
    path('emprendimientos/', include('apps.empr.urls')),

    #url de contactos
    path('contactos/', include('apps.contactos.urls')),

    path('comentarios/', include('apps.comentarios.urls')),

    path('perfil-usuario/', views.Perfil_usuario, name='perfil'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)