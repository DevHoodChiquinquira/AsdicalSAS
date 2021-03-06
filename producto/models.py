# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import signals
from django.db import models
import decimal
from django.db.models import signals

IVA_VALUE = 0.19

class Producto(models.Model):
	codigo = models.CharField(max_length=25,
		unique=True, verbose_name="Código")
	producto = models.CharField(max_length=45, unique=True,
		verbose_name="Producto")
	descripcion = models.CharField(max_length=45,
		verbose_name="Descripción")
	cantidad = models.PositiveSmallIntegerField(verbose_name="cantidad")
	valorIva = models.DecimalField(max_digits=15,
		decimal_places=2, default=0.00, verbose_name="IVA")
	valorVenta = models.DecimalField(max_digits=15,
		decimal_places=2, default=0.00, verbose_name="Valor de venta")

	def __unicode__(self):
		return self.producto

	def save(self, *args, **kwargs):
		if self.valorVenta:
			self.valorIva = round(float(self.valorVenta) * IVA_VALUE, 3)
			super(Producto, self).save(*args, **kwargs)
		else:
			self.valorIva=0
			super(Producto,self).save(*args, **kwargs)
