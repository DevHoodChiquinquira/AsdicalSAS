# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
#from recursos import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^cliente/new', views.ClienteInsert.as_view(), name='cliente_insert'),
    url(r'^cliente/list', views.ClienteList.as_view(), name='cliente_listar'),
    url(r'^cliente/update(?P<pk>[0-9]+)/$', views.ClienteUpdate.as_view(),
        name='cliente_update'),
    url(r'^cliente/detail(?P<pk>[0-9]+)/$', views.clienteDetail,
        name='cliente_detalle'),

]
