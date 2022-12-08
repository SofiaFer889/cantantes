from django.db import models

# Create your models here.
class Album(models.Model):
    nombre_album = models.CharField('nombre del album', max_length=100)
    
    def __str__(self):
        return self.nombre_album 
    
class Artista(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    #foto = models.ImageField()
    dni = models.PositiveIntegerField()
    fecha_de_nacimiento = models.DateField()
    sueldo_mensual = models.PositiveIntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nombre 
    
class Empresa(models.Model):
    nombre_empresa = models.CharField('nombre de la empresa', max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_empresa + '-' + self.artista.nombre