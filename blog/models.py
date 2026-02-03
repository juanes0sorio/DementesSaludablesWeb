from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    ESTADO_CHOICES = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, blank=True, help_text="Se genera del titulo automaticamente")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    contenido = RichTextField(verbose_name="Contenido del articulo")

    categorias =models.ManyToManyField(Categoria, verbose_name="Categorias", related_name="get_publicacion")
    imagen = models.ImageField(upload_to="blog/", verbose_name="Imagen", blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, verbose_name="Estado", default="borrador")

    class Meta:
        ordering = ['-creado']
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo