"""
URL configuration for dementesSaludables project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PublicacionSitemap
from django.http import HttpResponse

sitemaps = {'blog': PublicacionSitemap}

def llms_txt(request):
    # El formato Markdown es el estándar para llms.txt
    content = """# Dementes Saludables
    Portal especializado en salud mental y bienestar psicológico.

    ## Secciones Principales
    - [/blog/]: Artículos sobre psicología, consejos de bienestar y noticias.
    - [/]: Pagina principal

    ## Recursos para LLMs
    - Sitemap: /sitemap.xml
    - Este sitio sigue estándares de accesibilidad y contenido estructurado para facilitar la lectura por agentes de IA.
    """
    return HttpResponse(content, content_type="text/plain; charset=utf-8")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('llms.txt', llms_txt, name='llms_txt'),
    path('robots.txt', include('robots.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)