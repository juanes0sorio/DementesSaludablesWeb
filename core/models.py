from django.db import models

# Create your models here.
class Suscriptor(models.Model):
    email = models.EmailField(unique=True, verbose_name="Correo electronico")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de suscripcion")

    class Meta:
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"
        ordering = ['-creado']

    def __str__(self):
        return self.email
