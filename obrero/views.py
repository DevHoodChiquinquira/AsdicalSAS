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

#Permisos
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.decorators import (
    login_required, permission_required)


class ObreroInsert(LoginRequiredMixin,
                   PermissionRequiredMixin, CreateView):
    permission_required = ('obrero.add_obrero')
    model = Obrero
    success_url = reverse_lazy('cliente:obrero_listar')
    fields = ['dni', 'nombre', 'apellido', 'telefono', 'correo',
              'ciudad', 'direccion', 'banco', 'tipoCuenta',
              'numeroCuenta', ]

class ObreroList(LoginRequiredMixin, PermissionRequiredMixin,
                 ListView):
    permission_required = ('obrero.add_obrero')
    model = Obrero
    context_object_name = 'obreros'

class ObreroUpdate(LoginRequiredMixin, PermissionRequiredMixin,
                   UpdateView):
    permission_required = ('obrero.change_obrero')
    model = Obrero
    success_url = reverse_lazy('cliente:obrero_listar')
    fields = ['dni', 'nombre', 'apellido', 'telefono', 'correo',
              'ciudad', 'direccion', 'banco', 'tipoCuenta',
              'numeroCuenta', ]

@login_required()
def obreroDetail(request, pk):
    obrero = get_object_or_404(Obrero, pk=pk)
    template = loader.get_template('obrero/obrero_detail.html')
    context = {'obrero':obrero}
    return HttpResponse(template.render(context, request))
