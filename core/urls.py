from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobremi/', views.sobremi, name='sobremi'),
    path('politica-de-privacidad/', views.politica_privacidad, name='politica_privacidad'),


]