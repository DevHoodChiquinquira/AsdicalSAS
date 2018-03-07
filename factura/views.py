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
from producto.models import Producto
from obrero.models import Obrero
from .models import Obra, DetalleObra, DetalleObreroObra
from .models import Obra as ObraModel
import json
import decimal
from django.core import serializers
#para facturaCrear
from django.template import RequestContext
from django.db import transaction
from django.contrib import messages
from django.template import RequestContext as ctx
from django.template import Context
from .forms import RangoForm, FilterEstado, FilterEstadoObrero#, FiltroEstadoObreros
from django.utils import timezone

#Permisos
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.decorators import (
    login_required, permission_required)




#class para agregar un producto a una obra activa - form.py
class ProductoAdd(CreateView):
    permission_required = ('factura.change_detalleobra')
    template_name = 'factura/detalleobra_form.html'
    form_class = FilterEstado
    success_url = reverse_lazy('factura:obra_list')
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(ProductoAdd, self).form_valid(form)


class ObraUpdate(UpdateView):
    permission_required = ('factura.change_obra')
    model = Obra
    fields = ['descripcion', 'direccion', 'fechaInicio', 'fechaFinalizacion',
              'formaPago', 'estado',]
    success_url = reverse_lazy('factura:obra_list')

class ObreroAdd(CreateView):
    permission_required = ('factura.add_detalleobreroobra')
    template_name = 'factura/addobrero_form.html'
    form_class = FilterEstadoObrero
    success_url = reverse_lazy('factura:obra_list')
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(ObreroAdd, self).form_valid(form)

from django.http import JsonResponse

def searchObreroSelect(request):
    # if request.is_ajax():
    select_Obra = request.GET.get("obra")
    print(select_Obra)
    print("codigo")
    lista_obrero= Obrero.objects.exclude(detalleobreroobra__obra__id=select_Obra)
    json = serializers.serialize('json', lista_obrero,fields = ( 'id', 'dni', 'nombre','apellido'))
    print (json)
    return HttpResponse(json, content_type='application/json')
    # else:
    #     return HttpResponse("Solo ajax")
    # select_Obra = request.GET.get('select_Obra')
    # print(selectObra)
    # lista_obrero= Obrero.objects.none()
    # options = '<option value="" selected="selected">---------</option>'
    # if select_Obra:
    #     lista_obrero= Obrero.objects.exclude(detalleobreroobra__obra__id=select_Obra)
    # for obrero in lista_obrero:
    #     options += '<option value="%s">%s</option>' % (
    #         obrero.pk,
    #         obrero.nombre
    #     )
    # response = {}
    # response['lista_obrero'] = options
    # return HttpResponse(json.dumps(response), content_type='application/json')aca terminaba
    # lista_obrero= Obrero.objects.exclude(detalleobreroobra__obra__id=selectObras)
    # result = []
    # auxiliar = []
    # print(lista_obrero)

    # for obrero in lista_obrero:
    #     obrero_json={}
    #     obrero_json['id']=obrero.id
    #     # obrero_json['dni']= obrero.dni
    #     # obrero_json['nombre'] = obrero.nombre
    #     auxiliar.append(obrero_json)
    # for i in auxiliar:
    #     if i not in result:
    #         result.append(i)
    # data = json.dumps(result)
    #
    #
    #
    # return HttpResponse(data, mimetype)



# def addObreros(request):
#     form = FiltroEstadoObreros()
#     if request.method == 'POST':
#         form = FiltroEstadoObreros(request.POST)
#         if form.is_valid():
#             success_url = reverse_lazy('factura:obra_list')
#     return render (request, 'factura/addobreros_form.html',
#                    {'form':form})


@login_required()
@permission_required('factura.add_obra')
def obraCrear(request):
    form = None
    if request.method == 'POST':
        sid = transaction.savepoint()
        try:
            proceso = json.loads(request.POST.get('proceso'))
            print proceso
            print("en try")
            if 'clienProv' not in proceso:
                msg = 'El cliente no ha sido selecionado'
                raise Exception(msg)
            # if len(proceso['producto'])<=0:
            #     msg = 'No se ha selecionado ningun producto'
            #     raise Exception(msg)
            # if len(proceso['obrero']) <=0:
            #     msg = 'No selecciono ningun obrero'
            #     raise Exception(msg)
            #hasta aca era lo de obligatorio

            # for k in proceso['producto']:
            #     print(k['codigo'])
            #     producto = producto.objects.get(codigo=k['codigo'])

            crearObra = Obra(
                cliente = Cliente.objects.get(dni = proceso['clienProv']),
                fecha = timezone.now(),
                usuario = request.user,
                descripcion= proceso['descripcion'],
                direccion= proceso['direccion'],
                fechaInicio= proceso['fechaInicio'],
                fechaFinalizacion= proceso['fechaFinal'],
                porcentajeA= proceso['porcentajeA'],
                valorA= proceso['valorA'],
                porcentajeI= proceso['porcentajeI'],
                valorI= proceso['valorI'],
                porcentajeU= proceso['porcentajeU'],
                valorU= proceso['valorU'],
                formaPago= proceso['tipoPago'],
                iva= proceso['ivaU'],
                subtotal= proceso['subtotal'],
                total= proceso['total'],
                estado= proceso['estado'],
            )
            crearObra.save()
            print "factura Guardada"
            print crearObra
            for k in proceso['producto']:
                producto = Producto.objects.get(codigo=k['codigo'])
                print(producto)
                crearDetalleProducto = DetalleObra(
                    producto = producto,
                    usuario = request.user,
                    descripcion = producto.descripcion,
                    cantidad = int(k['cantidad']),
                    fecha = timezone.now(),
                    obra = crearObra,
                )
                crearDetalleProducto.save()
                print("Despues de crearDetalleProducto")
            for i in proceso['obrero']:
                obrero = Obrero.objects.get(dni=i['dni'])
                print(obrero)
                crearDetalleObrero = DetalleObreroObra(
                    obra = crearObra,
                    obrero = obrero,
                    usuario = request.user,
                )
                crearDetalleObrero.save()
            messages.success(request, 'La venta se ha realizado')
        except Exception, e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.error(request, e)
    return render(request, 'factura/crear_factura.html', {} )


class ObraList(LoginRequiredMixin, PermissionRequiredMixin,
               ListView):
    permission_required = ('factura.add_obra')
    model = Obra
    context_object_name = 'obras'
    paginate_by = 5
    #ordenar de mayor a menor
    def get_queryset(self, *args, **kwargs):
        qs = super(ObraList, self).get_queryset(*args, **kwargs).order_by("-id")
        return qs
    def get_context_data(self, **kwargs):
        context= super(ObraList, self).get_context_data(**kwargs)
        context['range'] = range(context["paginator"].num_pages)
        return context

@login_required()
def searchCliente(request):
    dni = request.GET.get('dni')
    dnis = Cliente.objects.filter(dni=dni)
    dnis = [cliente_serializer(cliente) for cliente in dnis]
    return HttpResponse(json.dumps(dnis), content_type='application/json')

def cliente_serializer(cliente):
    return{'dni':cliente.dni, 'nombreEmpresa':cliente.nombreEmpresa,
           'nombreRepresentante':cliente.nombreRepresentante,
           'apellidoRepresentante':cliente.apellidoRepresentante}

@login_required()
def searchProducto(request):
    codigo = request.GET.get('codigo')
    codigos = Producto.objects.filter(codigo=codigo)
    json = serializers.serialize('json', codigos,
                                 fields = ('codigo', 'producto',
                                           'descripcion', 'cantidad'))
    return HttpResponse(json, content_type='application/json')

@login_required()
def searchObrero(request):
    dni = request.GET.get('dniObrero')
    dnis = Obrero.objects.filter(dni=dni)
    json = serializers.serialize('json', dnis,
                                 fields = ('dni', 'nombre',
                                           'apellido', 'telefono'))
    return HttpResponse(json, content_type='application/json')



#pdf's
#Funciones de Creacion de PDF
def write_pdf(template_src, context_dict):
    template = loader.get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("utf-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(),
                                 content_type = 'application/pdf')
    return http.HttpResponse('ocurrio un error al generar el reporte %s'% cgi.escape(html))


class PdfObra(LoginRequiredMixin, TemplateView):
    # permission_required = ('factura.add_factura')
    def post(self, request, *args, **kwargs):
        buscar = request.POST['busqueda']
        print(buscar)
        obra = Obra.obraActiva.filter(id=buscar)
        detalleObra = DetalleObra.objects.filter(obra=buscar).order_by("-producto")
        detalleObreroObra = DetalleObreroObra.objects.filter(obra=buscar)


        return write_pdf('factura/obra_Detalle.html',
                         { 'obra':obra, 'detalleObra':detalleObra, 'pagesize':'A4',
                          'detalleObreroObra':detalleObreroObra})
