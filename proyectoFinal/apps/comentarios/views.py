from django.shortcuts import render
from django.contrib import messages
from apps.empr.models import Emprendimientos
from apps.comentarios.models import Comentarios
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
#CONTROLA SI EL USUARIO ESTA LOGEADO
from django.contrib.auth.mixins import LoginRequiredMixin
#controla que el user sea staff
from django.contrib.auth.mixins    import UserPassesTestMixin
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
'''
class CrearComentario(View, LoginRequiredMixin):
    def post(self, request, pk):
        # OBTENER DATOS A GUARDAR
        com = request.POST.get('comentario', None)
        usuario = request.user
        emprendimiento = Emprendimientos.objects.get(id=pk)

        comentario = Comentarios.objects.create(texto=com, usuario=usuario, emprendimiento=emprendimiento)

        # Devolvemos un JSON con el ID del comentario recién creado
        return JsonResponse({'comentario_id': comentario.pk})
''' 
@method_decorator(csrf_exempt, name='dispatch')
class CrearComentario(View, LoginRequiredMixin):
    def post(self, request, pk):
        try:
            # OBTENER DATOS A GUARDAR
            com = request.POST.get('comentario', None)
            usuario = request.user
            emprendimiento = Emprendimientos.objects.get(id=pk)
            
            comentario = Comentarios.objects.create(texto=com, usuario=usuario, emprendimiento=emprendimiento)
            messages.success(request, 'Comentario elimimnado con exito!.')
            
            # Devolvemos una respuesta JSON con los detalles del comentario recién creado
            data = {
                'texto': comentario.texto,
                'usuario': comentario.usuario.username,
            }
            return JsonResponse(data, status=201)  # Código de estado 201 Created

        except Emprendimientos.DoesNotExist:
            return JsonResponse({'error': 'Emprendimiento no encontrado'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

#elimina el comentario recibindo el pk por post y por url
@method_decorator(csrf_exempt, name='dispatch')
class EliminarComentario(LoginRequiredMixin, View):
    def post(self, request):
        try:#Obtenemos el pk y lo guardamos en una variable
            comentario_id = request.POST.get('comentario_id', None)
            #Buscamos segun el id obtenido
            comentario = Comentarios.objects.get(pk=comentario_id)
            #eliminamos
            comentario.delete()
            messages.success(request, 'Comentario elimimnado con exito!.')
            return JsonResponse({'messages': 'Comentario eliminado exitosamente'})
        except Comentarios.DoesNotExist:
            return JsonResponse({'error': 'Comentario no encontrado'}, status=404)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)





    