#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
#importar http
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
#Vistas
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    UpdateView,
    CreateView,
    DeleteView
    )
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
#mixins
from django.contrib.auth.mixins import(
    LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.decorators import (
    login_required, permission_required)
#pdf Dionicio
import datetime
#por defecto se instala html5lib==0.999999999
#para que funciones pip install html5lib==1.0b8
import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
from django import http
import cgi
#modelos
from cliente.models import Cliente
import json
import decimal
from django.core import serializers
#para facturaCrear
from django.template import RequestContext
from django.db import transaction
from django.contrib import messages
from django.template import RequestContext as ctx
from django.template import Context
from .forms import RangoForm
from django.utils import timezone

# Create your views here.

def obraCrear(request):
    form = None
    return render(request, 'factura/crear_factura.html', {} )


def searchCliente(request):
    dni = request.GET.get('dni')
    dnis = Cliente.objects.filter(dni__contains=dni)
    dnis = [cliente_serializer(cliente) for cliente in dnis]
    return HttpResponse(json.dumps(dnis), content_type='application/json')

def cliente_serializer(cliente):
    return{'dni':cliente.dni, 'nombreEmpresa':cliente.nombreEmpresa,
           'nombreRepresentante':cliente.nombreRepresentante,
           'apellidoRepresentante':cliente.apellidoRepresentante}
