# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Perfil(models.Model):
    numeroDocumento = models.CharField(max_length=15, unique=True,
                                       verbose_name="Número de Documento")
    telefono = PhoneNumberField(default='+573001234567', null=True,
                                verbose_name="Télefono")
    direccion = models.CharField(max_length=15, null=True,
                                 verbose_name="Dirección")
    user = models.OneToOneField(User, verbose_name= "Usario")
    imagen = models.ImageField(blank=True, null=True, upload_to="perfil")

    def __unicode__(self):
        return self.user.username
