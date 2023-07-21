from apps.empr.models import Categoria, Emprendimientos, User


def categorias_processor(request):
    categorias = Categoria.objects.all()
    num_categorias = len(categorias)
    return {
        'categorias': categorias,
        'num_categorias': num_categorias,
    }
    
def emprendimientos_processor(request):
    emprendimientos = Emprendimientos.objects.all()
    num_emprendimientos = len(emprendimientos)
    return{
        'emprendimientos': emprendimientos,
        'num_emprendimientos': num_emprendimientos,
    }
    
def usuarios_processor(request):
    usuarios = User.objects.all()
    num_usuarios = len(usuarios)
    return{
        'num_usuarios': num_usuarios
    }