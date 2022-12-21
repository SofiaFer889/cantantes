from django import forms
from .models import Artista, Album, Empresa

class ArtistaCreateForm(forms.ModelForm):
    
    class Meta:
        
     model = Artista
     fields = ('__all__')
     
class AlbumsCreateForm(forms.ModelForm):
   
   class Meta:
      
      model = Album
      fields = ('__all__')
      
class EmpresaCreateForm(forms.ModelForm):
       
   class Meta:
      
      model = Empresa
      fields = ('__all__')     
