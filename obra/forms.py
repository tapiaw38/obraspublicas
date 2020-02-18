from django import forms
from obra.models import Obra

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra

        fields = [
            'fecha',
            'usuario',
            'ubicacion_obra',
            'dias',
        ]

        labels = {
            'fecha':'Fecha y hora de inspección',
            'usuario':'Usuario',
            'ubicacion_obra':'Ubicacion de la obra',
            'dias':'Dias de plazo',
        }

        widgets = {
            'fecha' : forms.DateTimeInput(),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'ubicacion_obra': forms.TextInput(attrs={'class': 'form-control'}),
            'dias': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PresentaForm(forms.ModelForm):
    class Meta:
        model = Obra

        fields = [
            'presentacion',
            'fecha_presenta',
        ]

        labels = {
            'presentacion': 'Presentación',
            'fecha_presenta':'Fecha de presentación',
        }

        widgets = {
            'presentacion': forms.NullBooleanSelect(),
            'fecha_presenta' : forms.SelectDateWidget(),
        }