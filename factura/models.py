# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from cliente.models import Cliente
from producto.models import Producto
from obrero.models import Obrero
import decimal
from django.db.models import signals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.db import IntegrityError
import usuario.urls


class EstadoActivoObras(models.Manager):
    def get_query_set(self):
        return super(EstadoActivoObras, self).get_query_set().filter(estado='activo')

class Obra(models.Model):
    FORMA_PAGO= (('efectivo', 'Efectivo'), ('cheque', 'Cheque'),
                 ('tarjeta débito', 'Tarjeta débito'),
                 ('tarjeta crédito', 'Tarjeta crédito'),
                 ('venta a crédito','Venta a crédito'),
                 ('bono','Bono'),('vale','Vale'), ('otros','Otros'),)
    PORCENTAJE= ((0,'0%'),(1,'1%'),(2,'2%'),(3,'3%'),(4,'4%'),(5,'5%'),
                     (6,'6%'),(7,'7%'),(8,'8%'),(9,'9%'),(10,'10%'),(11,'11%'),
                     (12,'12%'),(13,'13%'),(14,'14%'),(15,'15%'),(16,'16%'),(17,'17%'),)
    ESTADO_OBRA = (('activo', 'Activo'), ('finalizado', 'Finalizado'))

    descripcion = models.CharField(max_length=45, verbose_name="Descripción")
    direccion = models.CharField(max_length=45, verbose_name="Dirección")
    fecha = models.DateField(auto_now_add=True)#fecha de Venta
    fechaInicio = models.DateField(auto_now_add=False,
        verbose_name="Fecha Inicio")
    fechaFinalizacion = models.DateField(auto_now_add=False,
        verbose_name="Fecha Finalización")
    porcentajeA = models.PositiveSmallIntegerField(choices=PORCENTAJE,
        null=True, blank=True, verbose_name= 'Porcentaje A')
    valorA = models.DecimalField(max_digits=15, default=0,
        decimal_places=2, null=True, blank=True, verbose_name='Valor A')
    porcentajeI = models.PositiveSmallIntegerField(choices=PORCENTAJE,
        null=True, blank=True, verbose_name= 'Porcentaje I')
    valorI = models.DecimalField(max_digits=15, default=0,
        decimal_places=2, null=True, blank=True, verbose_name='Valor I')
    porcentajeU = models.PositiveSmallIntegerField(choices=PORCENTAJE,
        null=True, blank=True, verbose_name= 'Porcentaje U')
    valorU = models.DecimalField(max_digits=15, default=0,
        decimal_places=2, null=True, blank=True, verbose_name='Valor U')
    formaPago = models.CharField(choices=FORMA_PAGO ,max_length=50,
        verbose_name='Forma de pago')
    iva = models.DecimalField(max_digits=15, decimal_places=2, default=0,
        null=True, blank=True, verbose_name='Iva U')
    subtotal = models.DecimalField(max_digits=15, default=0,
		decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=15, default=0,
		decimal_places=2, null=True, blank=True)
    usuario = models.ForeignKey(User)
    cliente = models.ForeignKey(Cliente)
    estado = models.CharField(choices=ESTADO_OBRA, max_length=20)
    obraActiva = EstadoActivoObras()

    def __unicode__(self):
		return u'id: %s obra: %s Fechas: %s -  %s'%( self.id, self.descripcion,
                   self.fechaInicio, self.fechaFinalizacion)


class DetalleObra(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto)
    usuario = models.ForeignKey(User)
    descripcion = models.CharField(max_length=45,
        verbose_name="Descripción")
    cantidad = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="cantidad")
    fecha = models.DateField(auto_now_add=True)#fecha despacho
    valor = models.DecimalField(max_digits=15, default=0,
        decimal_places=2, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s'%(self.obra, self.descripcion)

class DetalleObreroObra(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    obrero = models.ForeignKey(Obrero)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s %s'%(self.obra, self.obrero)
