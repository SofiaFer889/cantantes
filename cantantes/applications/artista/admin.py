from django.contrib import admin
# Register your models here.
from .models import (
    Artista,
    Album,
    Empresa
)
admin.site.register(Album)
admin.site.register(Empresa)

class ArtistaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'dni',
        'fecha_de_nacimiento',
        'sueldo_mensual',
    )
    search_fields = ('nombre',)
    list_filter = ('sueldo_mensual',)
admin.site.register(Artista, ArtistaAdmin)
