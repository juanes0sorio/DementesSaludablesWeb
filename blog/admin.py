from django.contrib import admin
from .models import Publicacion, Categoria


# Register your models here.

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo',
                    'estado',
                    'creado',
                    'autor')
    list_filter = ('estado',
                   'creado')
    search_fields = ('titulo',
                     'contenido')

    prepopulated_fields = {'slug': ('titulo',)}

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


