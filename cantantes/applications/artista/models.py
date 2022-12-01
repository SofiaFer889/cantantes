from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    foto = models.ImageField()
    dni = models.PositiveIntegerField()
    fecha_de_nacimiento = models.DateField()
    sueldo_mensual = models.PositiveIntegerField()
    
    def __str__(self):
        return self.apellido + '-' + self.nombre