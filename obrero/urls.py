# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
#from recursos import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^new', views.ObreroInsert.as_view(), name='obrero_insert'),
    url(r'^list', views.ObreroList.as_view(), name='obrero_listar'),
    url(r'^update(?P<pk>[0-9]+)/$', views.ObreroUpdate.as_view(),
        name='obrero_update'),
    url(r'^detail(?P<pk>[0-9]+)/$', views.obreroDetail,
        name='obrero_detalle'),

]
