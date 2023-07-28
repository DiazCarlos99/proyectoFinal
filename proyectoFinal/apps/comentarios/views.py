from django.shortcuts import render
from django.contrib import messages
from apps.empr.models import Emprendimientos
from apps.comentarios.models import Comentarios
from django.views.generic import DeleteView, UpdateView

#CONTROLA SI EL USUARIO ESTA LOGEADO
from django.contrib.auth.mixins import LoginRequiredMixin
#controla que el user sea staff
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
    
    
        
def detalle_comentario(request):
    comentario_id = request.GET.get('comentario_id', None)
    try:
        comentario = Comentarios.objects.get(pk=comentario_id)
    except Comentarios.DoesNotExist:
        return JsonResponse({'error': 'Comentario no encontrado'}, status=404)

    return JsonResponse({'texto': comentario.texto})
   
   
    
@method_decorator(csrf_exempt, name='dispatch')
class ModificarComentario(View):
    def post(self, request):
        try:
            # Obtenemos el pk del comentario a actualizar y el nuevo contenido
            comentario_id = request.POST.get('comentario_id', None)
            nuevo_contenido = request.POST.get('nuevo_contenido', None)
            # Buscamos el comentario según el id obtenido
            comentario = Comentarios.objects.get(pk=comentario_id)

            # Actualizamos el contenido del comentario
            comentario.texto = nuevo_contenido
            comentario.save()
            messages.success(request, 'Comentario modificado con exito!.')
            return JsonResponse({'message': 'Comentario actualizado exitosamente'})
        except Comentarios.DoesNotExist:
            return JsonResponse({'error': 'Comentario no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


    