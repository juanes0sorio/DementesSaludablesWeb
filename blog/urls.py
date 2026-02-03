from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('publicacion/<slug:slug>/', views.publicacion_detalle, name='publicacion_detalle'),
]