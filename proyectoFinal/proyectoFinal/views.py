from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def Home(request):

	return render(request,'index.html')

def Sobre_nosotros(request):

	return render(request,'sobre_nosotros.html')

def Contacto(request):

	return render(request,'contacto.html')

def Empr(request):

	return render(request,'empr.html')


@login_required
def Perfil_usuario(request):

    return render(request, 'perfil.html')