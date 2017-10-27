# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import (
    UpdateView, CreateView, DeleteView)
from django.views.generic import ListView
from .models import Producto
#from .forms import PerfilForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

class ProductoInsert(CreateView):
    model = Producto
    success_url = reverse_lazy('producto:producto_listar')
    fields = ['codigo', 'producto', 'descripcion', 'cantidad',
              'valorVenta' ,]

class ProductoList(ListView):
    model = Producto
    context_object_name = 'productos'

class ProductoUpdate(UpdateView):
    model = Producto
    success_url = reverse_lazy('producto:producto_listar')
    fields = ['codigo', 'producto', 'descripcion', 'cantidad',
              'valorVenta' ,]

def productoDetail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    template = loader.get_template('producto/producto_detail.html')
    context = {'producto':producto}
    return HttpResponse(template.render(context, request))
    
