from django.shortcuts import render, redirect
from blog.models import Publicacion
from .models import Suscriptor
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        if email:
            try:
                Suscriptor.objects.create(email=email)
                messages.success(request, 'Gracias por unirte a nuestra comunidad!')
            except IntegrityError:
                messages.warning(request, 'Este correo ya existe.')
            except Exception as e:
                messages.error(request, e)
        return redirect('home')

    publicaciones = Publicacion.objects.filter(estado='publicado').order_by('-creado')[:3]
    return render(request, 'core/home.html', {'publicaciones': publicaciones})

def sobremi(request):
    return render(request, 'core/sobremi.html')