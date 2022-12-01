from django.db import models
from applications.artista.models import Artista


class Empresa(models.Model):
    nombre_empresa = models.CharField('nombre de la empresa', max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_empresa + '-' + self.artista.nombre