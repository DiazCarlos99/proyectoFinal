from django.shortcuts import render


def Home(request):

	return render(request,'index.html')

def Sobre_nosotros(request):

	return render(request,'sobre_nosotros.html')

def Contacto(request):

	return render(request,'contacto.html')

def Ingresar(request):

	return render(request,'users/ingresar.html')

def Registrarse(request):

	return render(request,'users/registrarse.html')

def Noticias(request):

	return render(request,'post.html')