from django.contrib.sitemaps import Sitemap
from .models import Publicacion

class PublicacionSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    def items(self):
        return Publicacion.objects.all()

    def lastmod(self, obj):
        return obj.creado

    def location(self, obj):
        return f'/blog/{obj.slug}/'