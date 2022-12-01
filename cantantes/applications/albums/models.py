from django.db import models
from applications.artista.models import Artista
# Create your models here.
class Album(models.Model):
    nombre_album = models.CharField('nombre del album', max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_album + '-' + self.artista.nombre