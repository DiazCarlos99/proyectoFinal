from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

from .models import Emprendimientos, Categoria
from .forms import Form_Alta,  Form_Modificacion

#CONTROLA SI EL USUARIO ESTA LOGEADO
from django.contrib.auth.mixins import LoginRequiredMixin
#se importan los alert o mensajes
from django.contrib import messages
#controla que el user sea staff
from django.contrib.auth.mixins    import UserPassesTestMixin


class CrearEmpredimiento(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Emprendimientos
    form_class = Form_Alta 
    template_name = 'empr/crear.html' #nombre del template
    success_url = reverse_lazy('empr:listar_emprendimientos') #una vez creada la noticia a donde direcciona

    def test_func(self):
        return self.request.user.is_staff
    
    def form_valid(self, form):
        emprendimiento = form.save(commit=False)
        emprendimiento.autor = self.request.user
        return super(CrearEmpredimiento, self).form_valid(form)
    
        
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            # Si el usuario no tiene permiso, se muestra un mensaje de error
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        # Manejar el caso cuando el usuario no tiene los permisos necesarios
        return render(self.request, 'error/403.html', {'mensaje': 'No tienes permiso para acceder a esta página.'}, status=403)

    
    

    
class   ListarEmprendimientos(ListView):
    model = Emprendimientos
    template_name = 'empr/listar.html' 
    context_object_name = 'emprendimientos_por_categoria'
    
    def get(self, request, *args, **kwargs):
        emprendimiento_id = request.GET.get('emprendimiento_id')
        if emprendimiento_id:
            messages.success(request, 'El emprendimiento ha sido eliminado exitosamente.')
        return super().get(request, *args, **kwargs)

'''
def DetalleEmprendimientos(LoginRequiredMixin, request, pk):
	ctx = {}
	noti = Emprendimientos.objects.get(id = pk)
	ctx['emprendimiento'] = noti
	return render(request, 'empr/detalles.html', ctx)
'''

class DetalleEmprendimientos(DetailView):
    model = Emprendimientos 
    template_name = 'empr/detalles.html'

    
class EditarEmprendimientos(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Emprendimientos
    form_class = Form_Modificacion
    template_name = 'empr/editar.html'

        #FUNCION PARA DETERMINAR SI EL USUARIO ES STAFF
    def test_func(self):
        return self.request.user.is_staff
    
    def test_func_autor(self):
        # Verifica si el usuario actual es el autor del emprendimiento
        emprendimiento = self.get_object()
        return self.request.user == emprendimiento.autor
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar el ID del emprendimiento en el contexto
        context['emprendimiento_id'] = self.object.pk
        return context
    
    def get_success_url(self):
        # Redirigir a la página de detalles del emprendimiento editado
        emprendimiento_id = self.object.pk
        return reverse_lazy('empr:detalle_emprendimiento', kwargs={'pk': emprendimiento_id})
    
    def form_valid(self, form):
        # Lógica de actualización del emprendimiento
        messages.success(self.request, 'El emprendimiento ha sido actualizado exitosamente.')
        return super().form_valid(form)
    # Mensaje personalizado para el error de permisos
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            # Si el usuario no tiene permiso, se muestra un mensaje de error
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        # Manejar el caso cuando el usuario no tiene los permisos necesarios
        return render(self.request, 'error/403.html', {'mensaje': 'No tienes permiso para acceder a esta página.'}, status=403)


     
class EliminarEmprendimientos(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Emprendimientos
    template_name = 'empr/eliminar.html'
    success_url = reverse_lazy('empr:listar_emprendimientos')

    def test_func(self):
        return self.request.user.is_staff
    
    def test_func_autor(self):
        # Verifica si el usuario actual es el autor del emprendimiento
        emprendimiento = self.get_object()
        return self.request.user == emprendimiento.autor
    
    def delete(self, request, *args, **kwargs):
        # Obtenemos el emprendimiento que se va a eliminar
        emprendimiento = self.get_object()

        # Eliminamos el emprendimiento
        self.perform_destroy(emprendimiento)

        # Redireccionamos a la página de listar con el ID del emprendimiento eliminado
        return redirect('empr:listar_emprendimientos', emprendimiento_id=emprendimiento.pk)
    
    # Mensaje personalizado para el error de permisos
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            # Si el usuario no tiene permiso, se muestra un mensaje de error
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        # Manejar el caso cuando el usuario no tiene los permisos necesarios
        return render(self.request, 'error/403.html', {'mensaje': 'No tienes permiso para acceder a esta página.'}, status=403)

    
class  FiltrarEmprendimientos(ListView):
    model = Emprendimientos
    template_name = 'empr/filtrar.html'
    success_url = reverse_lazy('empr:filtrar_emprendimientos')
    context_object_name = 'emprendimientos_filtrados'
    
    def get_queryset(self):
        #obtenemos el valor de nombre desde la url
        nombre = self.kwargs.get('nombre')
        #filtramos segun id
        queryset = Emprendimientos.objects.filter(categoria__nombre=nombre)
        return queryset
    
class Categorias(ListView):
    model = Categoria
    template_name = 'empr/categorias.html'
    
class FiltrarPorAntiguedad(ListView):
    model = Emprendimientos
    template_name = 'empr/categorias.html'
    context_object_name = 'emprendimientos'
    
    def get_queryset(self):
        orden = self.kwargs.get('orden')
        
        if orden == 'asc':
            return Emprendimientos.objects.order_by('creado')
        elif orden == 'desc':
            return Emprendimientos.objects.order_by('-creado')
        
class FiltrarPorOrdenAlfabetico(ListView):
    model = Emprendimientos
    template_name = 'empr/categorias.html'
    context_object_name = 'emprendimientos'
    
    def get_queryset(self):
        orden = self.kwargs.get('orden')
        
        if orden == 'asc':
            return Emprendimientos.objects.order_by('titulo')
        elif orden == 'desc':
            return Emprendimientos.objects.order_by('-titulo')
        