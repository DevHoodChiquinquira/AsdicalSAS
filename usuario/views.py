# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import (
    UpdateView, CreateView, DeleteView)
from django.views.generic import ListView
from .models import Perfil
from .forms import PerfilForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
def authentication(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print (username)
        if action == 'login':
            #value de submit
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('usuario:sistema')
        return redirect('usuario:index')
    return render(request, 'login.html', {})

@login_required()
def systemIndex(request):
    return render (request, 'sistema.html', {})

class PerfilInsert(CreateView):
    model = Perfil
    success_url = reverse_lazy('usuario:perfil_listar')
    fields = ['numeroDocumento', 'telefono', 'direccion',
              'imagen',]
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PerfilInsert, self).form_valid(form)

class PerfilUpdate(UpdateView):
    model = Perfil
    success_url = reverse_lazy('usuario:perfil_listar')
    fields = ['numeroDocumento', 'telefono', 'direccion',
              'imagen',]
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PerfilUpdate, self).form_valid(form)

class PerfilList(ListView):
    model = Perfil
    context_object_name = 'perfiles'
    def get_queryset(self):
        return Perfil.objects.filter(user=self.request.user)


def perfilDetail(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    template = loader.get_template('usuario/perfil_detail.html')
    context = {'perfil':perfil}
    return HttpResponse(template.render(context, request))
