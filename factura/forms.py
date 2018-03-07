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





        # obrass = Obra.obraActiva.filter(estado="activo")
        # obrassS = obrass[0]
        # # obrerosIns = Obrero.objects.all()
        # # obrerosInss= obrerosIns[0]
        # print obrassS
        # print "algo"
        # # son = DetalleObreroObra.objects.select_related().filter(obra=obrassS).exclude(obrero=obrerosInss)
        # son = DetalleObreroObra.objects.select_related().filter(obra=obrassS)
        # # son = DetalleObreroObra.objects.all()
        # sons= son[1]
        # print(sons)
        # print("nananananana")
        # obrerosIns = Obrero.objects.select_related().exclude(dni=sons.obrero)
        # # obrerosIns = Obrero.objects.select_related().exclude(dni=sons)
        # # obrerosInss= obrerosIns[0]
        # # print(obrerosInss)
        # self.fields['obrero'].queryset = obrerosIns


# class FiltroEstadoObreros(forms.Form):
#     obra = forms.ModelChoiceField(
#         label = u'Obra0',
#         queryset=Obra.obraActiva.all()
#     )
#     obrero = forms.ModelChoiceField(
#         label=u'Obrero',
#         queryset=Obrero.objects.all()
#     )
#     widget = {
#                 'obrero' : forms.RadioSelect(attrs={'class':'custom-select','id':'id_obrero'}),
#                 'obra' : forms.Select(attrs={'class': 'custom-select', 'id':'id_obra'}),
#             }
#     def __init__(self, *args, **kwargs):
#         super(FiltroEstadoObreros, self).__init__(*args, **kwargs)
#         self.fields['obra'].queryset = Obra.obraActiva.filter(estado="activo")
#         self.fields['obrero'].queryset = Obrero.objects.filter(dni="1")
#
#     #
#     # def __init__(self, *args, **kwargs):
#     #     super(UbicacionForm, self).__init__(*args, **kwargs)
#     #     self.fields['municipio'].queryset = Municipio.objects.none()
#     #     self.fields['localidad'].queryset = Localidad.objects.none()
