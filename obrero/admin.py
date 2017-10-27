# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Obrero
# Register your models here.

@admin.register(Obrero)
class AdminObrero(admin.ModelAdmin):
    list_display = ('id','dni', 'nombre', 'apellido',
                    'telefono',)
