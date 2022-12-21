from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
)


from .models import Artista, Album, Empresa
from .forms import ArtistaCreateForm, AlbumsCreateForm, EmpresaCreateForm

class ArtistaCreateView(CreateView):
    template_name = "artista/add.html"
    model = Artista
    form_class = ArtistaCreateForm
    success_url = reverse_lazy('artista_app:lista-user')

    
class ArtistaUpdateView(UpdateView):
    model = Artista
    template_name = "artista/update.html"
    fields = [
        'nombre',
        'apellido',
        'dni',
        'fecha_de_nacimiento',
        'sueldo_mensual',
        'album',
    ]
    success_url = reverse_lazy('artista_app:lista-user')
    
class ArtistaListView(ListView):
    template_name = "artista/lista.html"
    context_object_name = 'artista'
    
    def get_queryset(self):
        return Artista.objects.all
    
class ArtistaListBykword(ListView):
    template_name = "artista/lista_nombre.html"
    context_object_name = 'artista'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Artista.objects.filter(
            nombre = palabra_clave
        )
        return lista
    
    
class AlbumsCreateView(CreateView):
    template_name = "albums/add.html"
    form_class = AlbumsCreateForm
    success_url = reverse_lazy('artista_app:album-user')
    
    
class AlbumListView(ListView):
    template_name = "albums/album_view.html"
    context_object_name = 'album'
    
    def get_queryset(self):
        return Album.objects.all
    
    
class EmpresaCreateView(CreateView):
    template_name = "empresa/add.html"
    form_class = EmpresaCreateForm
    success_url = reverse_lazy('artista_app:empresa-user')
    
    
class EmpresaListView(ListView):
    template_name = "empresa/empresa_view.html"
    context_object_name = 'empresa'
    
    def get_queryset(self):
        return Empresa.objects.all
    
    
class ConsultaJoinn(ListView):
    template_name = "artista/join.html"
    context_object_name = 'artistas'
    
    def get_queryset(self):
        artistas = Artista.objects.select_related().all()
        return artistas


class HomeView(TemplateView):
    template_name = "artista/home.html"
    


def aumentar(salario, x):
    nuevoSalario = salario + (salario * (x/100))
    return nuevoSalario
    
salarioActual = float(input("ingrese sueldo"))
incremento = float(input("ingrese numero"))
nuevoSalario = aumentar(salarioActual, incremento)
print(nuevoSalario)