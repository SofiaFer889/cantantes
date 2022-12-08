from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    View,
    CreateView,
    ListView,
    UpdateView,
)

from .models import Artista, Album, Empresa
from .forms import ArtistaCreateForm, AlbumsCreateForm

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
    success_url = reverse_lazy('artista_app:registro-album')
    
class EmpresaCreateView(CreateView):
    template_name = "empresa/add.html"
    form_class = AlbumsCreateForm
    success_url = reverse_lazy('artista_app:registro-empresa')
    
class Join(ListView):
    template_name = "artista/lista_join.html"
    context_object_name = 'artista'