from typing import Any
from django.db.models.query import QuerySet
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.shortcuts import render, redirect
import os

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse, reverse_lazy

from .models import Emprendimientos
from .forms import Form_Alta,  Form_Modificacion

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

from django.contrib.auth.mixins    import UserPassesTestMixin

from django.db.models import Func, F

class CrearEmpredimiento(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Emprendimientos
    form_class = Form_Alta
    template_name = 'empr/crear.html'

    def get_success_url(self):
        return reverse('empr:detalle_emprendimiento', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        emprendimiento = form.save(commit=False)
        emprendimiento.autor = self.request.user
        emprendimiento.save()
        messages.success(self.request, 'El emprendimiento ha sido creado exitosamente.')
        return super().form_valid(form)


    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
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

class DetalleEmprendimientos(DetailView):
    model = Emprendimientos
    template_name = 'empr/detalles.html'
    context_object_name = 'emprendimientos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class EditarEmprendimientos(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Emprendimientos
    form_class = Form_Modificacion
    template_name = 'empr/editar.html'

    def test_func(self):
        return self.request.user.is_staff

    def test_func_autor(self):
        emprendimiento = self.get_object()
        return self.request.user == emprendimiento.autor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emprendimiento_id'] = self.object.pk
        return context

    def get_success_url(self):
        emprendimiento_id = self.object.pk
        return reverse_lazy('empr:detalle_emprendimiento', kwargs={'pk': emprendimiento_id})

    def form_valid(self, form):
        messages.success(self.request, 'El emprendimiento ha sido actualizado exitosamente.')
        return super().form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        return render(self.request, 'error/403.html', {'mensaje': 'No tienes permiso para acceder a esta página.'}, status=403)



class EliminarEmprendimientos(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Emprendimientos
    template_name = 'empr/eliminar.html'
    success_url = reverse_lazy('empr:listar_emprendimientos')

    def test_func(self):
        return self.request.user.is_staff

    def test_func_autor(self):
        emprendimiento = self.get_object()
        return self.request.user == emprendimiento.autor
    @receiver(pre_delete, sender=Emprendimientos)
    def eliminar_imagen_emprendimiento(sender, instance, **kwargs):
        if instance.imagen:
            if os.path.isfile(instance.imagen.path):
                os.remove(instance.imagen.path)
    def delete(self, request, *args, **kwargs):
        emprendimiento = self.get_object()
        self.perform_destroy(emprendimiento)
        return redirect('empr:listar_emprendimientos', emprendimiento_id=emprendimiento.pk)

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        return render(self.request, 'error/403.html', {'mensaje': 'No tienes permiso para acceder a esta página.'}, status=403)


class FiltrarPorOrden(ListView):
    model = Emprendimientos
    template_name = 'empr/filtrar-orden.html'
    context_object_name = 'emprendimientos'
    def get_queryset(self):

        nombre = self.kwargs.get('nombre')

        if nombre:
            queryset = Emprendimientos.objects.filter(categoria__nombre=nombre)
        else:
            queryset = Emprendimientos.objects.all()

        orden = self.kwargs.get('orden')
        if orden == 'asc':
            queryset = queryset.order_by('titulo')
        elif orden == 'desc':
            queryset = queryset.order_by('-titulo')
        elif orden == 'antiguedad-asc':
            queryset = queryset.order_by('creado')
        elif orden == 'antiguedad-desc':
            queryset = queryset.order_by('-creado')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.kwargs.get('nombre')
        return context