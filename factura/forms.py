# -*- coding: utf-8 -*-
from .models import DetalleObra, Obra, DetalleObreroObra # Change as necessary
from obrero.models import Obrero
from django.forms import ModelForm
from django import forms


class RangoForm (forms.Form):
    fecha_i = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'Fecha_i', 'data-date-format':'dd/mm/yyyy'}))
    fecha_f = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'Fecha_f', 'data-date-format':'dd/mm/yyyy'}))

# https://stackoverflow.com/questions/24041649/filtering-a-model-in-a-createview-with-get-queryset
#formulario para filtrar solo muestra obras activas
class FilterEstado(forms.ModelForm):
    class Meta:
        model = DetalleObra
        fields = ['obra','producto', 'descripcion', 'cantidad',]

    def __init__(self, *args, **kwargs):
        super(FilterEstado, self).__init__(*args, **kwargs)
        self.fields['obra'].queryset = Obra.obraActiva.filter(estado="activo")


class FilterEstadoObrero(forms.ModelForm):
    class Meta:
        model = DetalleObreroObra
        fields = ['obra','obrero',]
        labels = {
            'obrero' : 'Obrero es ',
            'obra' : 'Selecciona Obra'
        }
        widget = {
            'obrero' : forms.RadioSelect(attrs={'class':'custom-select','id':'id_obrero'}),
            'obra' : forms.Select(attrs={'class': 'custom-select', 'id':'id_obra_o', 'name':'id_obra_o'}),
        }
    def __init__(self, *args, **kwargs):
        super(FilterEstadoObrero, self).__init__(*args, **kwargs)
        self.fields['obra'].queryset = Obra.obraActiva.filter(estado="activo")
        self.fields['obra'].widget.attrs.update({"class":"custom-select", 'id':'id_obra_o', 'name':'id_obra_o' })
        #self.fields['obrero'].queryset = Obrero.objects.none()
        self.fields['obrero'].widget.attrs.update({"class":"custom-select" })


class ModificarObra(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['descripcion','direccion','fechaInicio',
                  'fechaFinalizacion', 'porcentajeA', 'valorA',
                  'porcentajeI', 'valorI', 'porcentajeU', 'valorU',
                  'formaPago', 'iva', 'subtotal', 'total', 'estado',]
        # labels = {
        #     'descripcion' : 'Descripción ',
        #     'direccion' : 'Dirección',
        #     'fechaInicio' : 'Fecha Inicio',
        #     'fechaFinalizacion' : 'Fecha Finalización',
        #     'porcentajeA' : 'Porcentaje A',
        #     'valorA' : 'Valor A',
        #     'porcentajeI' : 'Porcentaje I',
        #     'valorI' : 'Valor I',
        #     'porcentajeU' : 'Porcentaje U',
        #     'valorU' : 'Valor U',
        #     'formaPago' : 'Forma de pago', 'iva': 'IVA',
        #     'subtotal': 'Sub-Total', 'total' : 'Total',
        #     'estado' : 'Estado', }
        # widget = {
        # }
    def __init__(self, *args, **kwargs):
        super(ModificarObra, self).__init__(*args, **kwargs)
