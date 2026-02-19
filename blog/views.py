from django.shortcuts import render, get_object_or_404
from .models import Publicacion, Categoria
from django.core.paginator import Paginator
from django.conf import settings
from django.core import signing
from django.http import HttpResponse
from core.models import Suscriptor

# Create your views here.
def blog_home(request):

    categorias = Categoria.objects.all()

    publicaciones_list = Publicacion.objects.filter(estado='publicado')

    categoria_id = request.GET.get('categoria')
    categoria_activa = None
    if categoria_id:
        publicaciones_list = publicaciones_list.filter(categorias__id=categoria_id)
        categoria_activa = Categoria.objects.filter(id=categoria_id).first()

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

def newsletter_baja(request, token):
    data = signing.loads(token, salt="newsletter-baja", max_age=60 * 60 * 24 * 30)
    email = data["email"]

    Suscriptor.objects.filter(email=email).delete()

    return render(request, "blog/baja_ok.html", {"email": email})


