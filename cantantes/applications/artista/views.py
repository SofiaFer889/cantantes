from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
)
from django.db.models import Max, Min

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
    
    
class AumentarSueldo(UpdateView):
    model = Artista
    template_name = "artista/update20.html"
    fields = [
        'sueldo_mensual',
        'id',
    ]
    success_url = reverse_lazy('artista_app:lista-user')

    def form_valid(self, form):
        salario = form.instance.sueldo_mensual
        x = 0.20
        salario_aumentado = salario + (salario * x)
        form.instance.sueldo_mensual = salario_aumentado
        form.save()

        return super().form_valid(form)
    
    
class AumentarSueldo2(UpdateView):
    model = Artista
    template_name = "artista/update15.html"
    fields = [
        'sueldo_mensual',
        'id',
    ]
    success_url = reverse_lazy('artista_app:lista-user')

    def form_valid(self, form):
        salario = form.instance.sueldo_mensual
        x = 0.15
        salario_aumentado = salario + (salario * x)
        form.instance.sueldo_mensual = salario_aumentado
        form.save()

        return super().form_valid(form)
    
    
class AumentarSueldo3(UpdateView):
    model = Artista
    template_name = "artista/update10.html"
    fields = [
        'sueldo_mensual',
        'id',
    ]
    success_url = reverse_lazy('artista_app:lista-user')

    def form_valid(self, form):
        salario = form.instance.sueldo_mensual
        x = 0.10
        salario_aumentado = salario + (salario * x)
        form.instance.sueldo_mensual = salario_aumentado
        form.save()

        return super().form_valid(form)  

    
class ArtistaListView(ListView):
    template_name = "artista/lista.html"
    context_object_name = 'artista'
    
    def get_queryset(self):
        return Artista.objects.all
    
   
class ContarArtistaListView(ListView):
    template_name = "artista/contar_lista.html"
    context_object_name = 'contar'

    def get_context_data(self, **kwargs):
        personas = super().get_context_data(**kwargs)
        personas['num_personas'] = Artista.objects.count()
        return personas

    def get_queryset(self):
        return []
    
    
class MayorSueldoListView(ListView):
    model = Artista
    template_name = "artista/mayor_sueldo.html"
    context_object_name = 'mayor'

    def get_queryset(self):
        mayor_sueldo = Artista.objects.aggregate(Max('sueldo_mensual'))['sueldo_mensual__max']
        return Artista.objects.filter(sueldo_mensual=mayor_sueldo)
    
    
class MenorSueldoListView(ListView):
    model = Artista
    template_name = "artista/menor_sueldo.html"
    context_object_name = 'menor'

    def get_queryset(self):
        menor_sueldo = Artista.objects.aggregate(Min('sueldo_mensual'))['sueldo_mensual__min']
        return Artista.objects.filter(sueldo_mensual=menor_sueldo)
        
        
class DiferenciaMayorMenorSueldo(ListView):
    model = Artista
    template_name = "artista/diferencia_sueldo.html"
    context_object_name = 'diferencia'

    def get_context_data(self, **kwargs):
        diferencia = super().get_context_data(**kwargs)
        mayor_sueldo = Artista.objects.aggregate(Max('sueldo_mensual'))['sueldo_mensual__max']
        menor_sueldo = Artista.objects.aggregate(Min('sueldo_mensual'))['sueldo_mensual__min']
        diferencia['diferencia'] = mayor_sueldo - menor_sueldo
        return diferencia
    
    
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
    
class SueldoAnual(ListView):
    model = Artista
    template_name = "artista/sueldo_anual.html"
    context_object_name = 'artistas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artistas = Artista.objects.all()
        artistas_info = []
        for artista in artistas:
            artista_info = {
               'nombre': artista.nombre,
               'apellido': artista.apellido,
               'sueldo_anual': artista.sueldo_mensual * 12,
            }
            artistas_info.append(artista_info)
        context['artistas_info'] = artistas_info
        return context
    

class CalcularEdad(ListView):
    model = Artista
    template_name = "artista/edad.html"
    context_object_name = 'artistas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artistas_edades'] = [(artista, artista.edad()) for artista in context['artistas']]
        return context