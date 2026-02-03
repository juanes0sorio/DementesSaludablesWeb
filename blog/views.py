from django.shortcuts import render, get_object_or_404
from .models import Publicacion, Categoria
from django.core.paginator import Paginator

# Create your views here.
def blog_home(request):

    categorias = Categoria.objects.all()

    publicaciones_list = Publicacion.objects.filter(estado='publicado')

    categoria_id = request.GET.get('categoria_id')
    categoria_activa = None
    if categoria_id:
        publicaciones_list = publicaciones_list.objects.filter(categorias__id=categoria_id)
        categoria_activa = Categoria.objects.get(id=categoria_id)

    paginator = Paginator(publicaciones_list, 9)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'blog/todos.html', {
        'page_obj': page_obj,
        'categorias': categorias,
        'categoria_activa': categoria_activa
    })

def publicacion_detalle(request, slug):
    publicacion = get_object_or_404(Publicacion, slug=slug, estado='publicado')

    return  render(request, 'blog/unosolo.html', {
        'publicacion': publicacion
    })

