# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
#from recursos import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^login/$',views.authentication, name='autenticacion'),
    url(r'^sistema', views.systemIndex, name='sistema'),
    url(r'^perfil/new', views.PerfilInsert.as_view(), name='perfil_insert'),
    url(r'^perfil/list', views.PerfilList.as_view(), name='perfil_listar'),
    url(r'^perfil/update(?P<pk>[0-9]+)/$', views.PerfilUpdate.as_view(),
        name='perfil_update'),
    url(r'^perfil/detail(?P<pk>[0-9]+)/$', views.perfilDetail,
        name='perfil_detalle'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/'}, name="cerrar_sesion"),

    url(r'^galeria_drywall', views.galeriaDrywall, name='galeria_drywall'),
    url(r'^galeria_aluminio', views.galeriaAluminio, name='galeria_aluminio'),
    url(r'^galeria_vidrio', views.galeriaVidrio, name='galeria_vidrio'),
    url(r'^galeria_diseno', views.galeriaDiseno, name='galeria_diseno'),
    url(r'^galeria_domotica', views.galeriaDomotica, name='galeria_domotica'),
    url(r'^quienes_somos', views.quienesSomos, name='quienes_somos'),
]
