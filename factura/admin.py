from django.contrib import admin
from .models import Obra, DetalleObra

@admin.register(Obra)
class AdminObra(admin.ModelAdmin):
    list_display = ('id','descripcion', 'direccion', 'usuario',
                    'cliente',)

@admin.register(DetalleObra)
class AdminDetalleObra(admin.ModelAdmin):
    list_display = ('id','obra', 'producto', 'usuario',
                    'fecha',)
