from django.contrib import admin
# Register your models here.
from .models import (
    Artista,
    Album,
    Empresa
)

admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Empresa)