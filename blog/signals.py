from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import signing

from .models import Publicacion
from core.models import Suscriptor


def build_absolute_url(path: str) -> str:
    base = getattr(settings, "SITE_URL", "").rstrip("/")
    return f"{base}{path}" if base else path


@receiver(post_save, sender=Publicacion)
def notificacion_nuevo(sender, instance: Publicacion, created, **kwargs):
    if instance.estado != "publicado" or instance.notificado:
        return

    emails = list(Suscriptor.objects.values_list("email", flat=True))
    if not emails:
        return

    post_url = build_absolute_url(
        reverse("publicacion_detalle", kwargs={"slug": instance.slug})
    )

    for email in emails:
        token = signing.dumps({"email": email}, salt="newsletter-baja")
        baja_url = build_absolute_url(
            reverse("newsletter_baja", kwargs={"token": token})
        )

        context = {
            "titulo": instance.titulo,
            "resumen": (instance.contenido or "")[:400] + "...",
            "url": post_url,
            "baja_url": baja_url,
        }

        html_content = render_to_string("emails/nuevo_post.html", context)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(
            subject= instance.titulo,
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    Publicacion.objects.filter(pk=instance.pk).update(notificado=True)

