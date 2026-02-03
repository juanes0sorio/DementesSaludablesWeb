from django.contrib import admin
from .models import Suscriptor

# Register your models here.
@admin.register(Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ('email', 'creado')
    search_fields = ('email',)
    readonly_fields = ('creado',)