from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    View,
    FormView,
    ListView,
    UpdateView,
)

from .models import Artista, Album, Empresa
from .forms import ArtistaCreateForm, AlbumsCreateForm

class ArtistaCreateView(FormView):
    template_name = "artista/add.html"
    form_class = ArtistaCreateForm
    success_url = reverse_lazy('artista_app:lista-user')
    
    def form_valid(self, form):
        
        Artista.objects.create_user(
            nombre=form.cleaned_data['nombre'],
            apellido=form.changed_data['apellido'],
        )
        
        return super(ArtistaCreateView, self).form_valid(form)
    
class ArtistaUpdateView(UpdateView):
    model = Artista
    template_name = "artista/update.html"
    fields = [
        'nombre',
        'apellido',
        'foto',
        'dni',
        'fecha_de_nacimiento',
        'sueldo_mensual',
    ]
    success_url = reverse_lazy('login_app:lista-user')
    
class ArtistaListView(ListView):
    template_name = "artista/lista.html"
    context_object_name = 'artista'
       
    def get_queryset(self):
        return Artista.objects.all()
    
class AlbumsCreateView(FormView):
    template_name = "albums/add.html"
    form_class = AlbumsCreateForm
    success_url = reverse_lazy('artista_app:registro-album')
    
    def form_valid(self, form):
        
        Album.objects.create_user(
            nombre_album=form.cleaned_data['nombre_album'],
            artista=form.changed_data['artista'],
        )
        
        return super(AlbumsCreateView, self).form_valid(form)
    
class EmpresaCreateView(FormView):
    template_name = "empresa/add.html"
    form_class = AlbumsCreateForm
    success_url = reverse_lazy('artista_app:registro-empresa')
    
    def form_valid(self, form):
        
        Empresa.objects.create_user(
            nombre_empresa=form.cleaned_data['nombre_empresa'],
            artista=form.changed_data['artista'],
        )
        
        return super(EmpresaCreateView, self).form_valid(form)
    