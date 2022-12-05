from django.urls import path, re_path

from . import views

app_name = 'artista_app'

urlpatterns = [
    path('registro/artista', views.ArtistaCreateView.as_view(), name='registro-artista'),
    path('actualizar/user/<pk>', views.ArtistaUpdateView.as_view(), name='update-user'),
    path('lista/user', views.ArtistaListView.as_view(), name='lista-user'),
]