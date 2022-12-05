from django import forms
from .models import Artista

class ArtistaCreateForm(forms.ModelForm):
    
    class Meta:
        
     model = Artista
     fields = (
        'nombre',
        'apellido',
        'foto',
        'dni',
        'fecha_de_nacimiento',
        'sueldo_mensual',
     )