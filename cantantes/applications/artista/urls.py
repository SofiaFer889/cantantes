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
    path('contar/artistas', views.ContarArtistaListView.as_view(), name='contar'),
    path('sueldo/mayor/artistas', views.MayorSueldoListView.as_view(), name='sueldo-mayor'),
    path('sueldo/menor/artistas', views.MenorSueldoListView.as_view(), name='sueldo-menor'),
    path('aumentar/20/<pk>', views.AumentarSueldo.as_view(), name='aumentar'),
    path('aumentar/15/<pk>', views.AumentarSueldo2.as_view(), name='aumentar2'),
    path('aumentar/10/<pk>', views.AumentarSueldo3.as_view(), name='aumentar3'),
    path('diferencia', views.DiferenciaMayorMenorSueldo.as_view(), name='diferencia'),
    path('sueldo/anual/artista', views.SueldoAnual.as_view(), name='sueldo-anual'),
    path('edad/artista', views.CalcularEdad.as_view(), name='edad'),
]