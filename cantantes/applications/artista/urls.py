from django.urls import path

from . import views

app_name = 'artista_app'

urlpatterns = [
    path('registro/artista', views.ArtistaCreateView.as_view(), name='registro-artista'),
    path('registro/album', views.AlbumsCreateView.as_view(), name='registro-album'),
    path('registro/empresa', views.EmpresaCreateView.as_view(), name='registro-empresa'),
    path('actualizar/user/<pk>', views.ArtistaUpdateView.as_view(), name='update-user'),
    path('lista/user', views.ArtistaListView.as_view(), name='lista-user'),
    path('lista/album', views.AlbumListView.as_view(), name='album-user'),
    path('lista/empresa', views.EmpresaListView.as_view(), name='empresa-user'),
    path('lista/user-nombre', views.ArtistaListBykword.as_view(), name='lista-user-nombre'),
    path('consulta/join', views.ConsultaJoinn.as_view(), name='join'),
    path('home', views.HomeView.as_view(), name='home'),
]