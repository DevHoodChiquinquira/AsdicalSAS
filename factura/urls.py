# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
#from recursos import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^obra_new$', views.obraCrear, name="obra_crear"),
    url(r'^search_cliente', views.searchCliente, name='search_cliente'),
]
