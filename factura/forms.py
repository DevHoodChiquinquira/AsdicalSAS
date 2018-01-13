from .models import DetalleObra, Obra # Change as necessary
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
