# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import (
    UpdateView, CreateView, DeleteView)
from django.views.generic import ListView
from .models import Obrero
#from .forms import PerfilForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

class ObreroInsert(CreateView):
    model = Obrero
    success_url = reverse_lazy('cliente:obrero_listar')
    fields = ['dni', 'nombre', 'apellido', 'telefono', 'correo',
              'ciudad', 'direccion', 'banco', 'tipoCuenta',
              'numeroCuenta', ]

class ObreroList(ListView):
    model = Obrero
    context_object_name = 'obreros'

class ObreroUpdate(UpdateView):
    model = Obrero
    success_url = reverse_lazy('cliente:obrero_listar')
    fields = ['dni', 'nombre', 'apellido', 'telefono', 'correo',
              'ciudad', 'direccion', 'banco', 'tipoCuenta',
              'numeroCuenta', ]

def obreroDetail(request, pk):
    obrero = get_object_or_404(Obrero, pk=pk)
    template = loader.get_template('obrero/obrero_detail.html')
    context = {'obrero':obrero}
    return HttpResponse(template.render(context, request))
