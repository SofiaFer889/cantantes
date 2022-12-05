from django import forms
from .models import Artista, Album, Empresa

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
     
class AlbumsCreateForm(forms.ModelForm):
   
   class Meta:
      
      model = Album
      fields = (
         'nombre_album',
         'artista',
      )
      
class AlbumsCreateForm(forms.ModelForm):
       
   class Meta:
      
      model = Empresa
      fields = (
         'nombre_empresa',
         'artista',
      )