from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Emprendimientos, Categoria
from .forms import Form_Alta,  Form_Modificacion

#CONTROLA SI EL USUARIO ESTA LOGEADO
from django.contrib.auth.mixins import LoginRequiredMixin

class CrearEmpredimiento(LoginRequiredMixin, CreateView):
    model = Emprendimientos
    form_class = Form_Alta
    template_name = 'empr/crear.html' #nombre del template
    success_url = reverse_lazy('empr:listar_emprendimientos') #una vez creada la noticia a donde direcciona

    def form_valid(self, form):
        emprendimiento = form.save(commit=False)
        emprendimiento.autor = self.request.user
        return super(CrearEmpredimiento, self).form_valid(form)
    
class   ListarEmprendimientos(ListView):
    model = Emprendimientos
    template_name = 'empr/listar.html'

def DetalleEmprendimientos(request, pk):
	ctx = {}
	noti = Emprendimientos.objects.get(id = pk)
	ctx['emprendimiento'] = noti
	return render(request, 'empr/detalles.html', ctx)

class EditarEmprendimientos(UpdateView):
    model = Emprendimientos
    form_class = Form_Modificacion
    template_name = 'empr/editar.html'
    success_url = reverse_lazy('empr:listar_emprendimientos')
    pk_url_kwarg = 'pk'   
    
class EliminarEmprendimientos(DeleteView):
    model = Emprendimientos
    template_name = 'empr/eliminar.html'
    success_url = reverse_lazy('empr:listar_emprendimientos')