from apps.empr.models import Categoria, Emprendimientos, User
from apps.comentarios.models import Comentarios
from django.db.models import Count
# Obtener categorías que tienen emprendimientos asociados


def categorias_con_emprendimientos():
    categorias = Categoria.objects.filter('emprendmientos')
    return categorias

def categorias_processor(request):
    cat_context = Categoria.objects.all()
    num_categorias = len(cat_context)
    return {
        'cat_context': cat_context,
        'num_categorias': num_categorias,
    }
    
def emprendimientos_processor(request):
    emprendimientos = Emprendimientos.objects.all()
    num_emprendimientos = len(emprendimientos)
    return{
        'empr_context': emprendimientos,
        'num_emprendimientos': num_emprendimientos,
    }
    
def usuarios_processor(request):
    usuarios = User.objects.all()
    num_usuarios = len(usuarios)
    return{
        'num_usuarios': num_usuarios
    }

def emprendimientos_categorias(request):
    categorias = Categoria.objects.filter(emprendimientos__isnull=False).distinct()
    emprendimientos_por_categoria = {}
    
    for cat in categorias:
        emprendimientos = Emprendimientos.objects.filter(categoria=cat)
        emprendimientos_por_categoria[cat] = emprendimientos
        
    return {'empr_cat': emprendimientos_por_categoria}