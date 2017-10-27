# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
#from recursos import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^new', views.ProductoInsert.as_view(), name='producto_insert'),
    url(r'^list', views.ProductoList.as_view(), name='producto_listar'),
    url(r'^update(?P<pk>[0-9]+)/$', views.ProductoUpdate.as_view(),
        name='producto_update'),
    url(r'^detail(?P<pk>[0-9]+)/$', views.productoDetail,
        name='producto_detalle'),

]
