from django import forms
from notifica.models import Notifica

class NotificaForm(forms.ModelForm):
    class Meta:
        model=Notifica

        fields = [
            'fecha',
            'lugar',
            'caracteristicas',
            'usuario',
            'hechos',
            'situacion',
        ]

        labels = {
            'fecha':'Fecha y Hora del Hecho',
            'lugar':'Lugar del Hecho',
            'caracteristicas':'Caracteristicas del Hecho',
            'usuario':'Usuario',
            'hechos':'Hechos Presuntamente Infraccionales',
            'situacion': 'Presentación',
        }

        widgets = {
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'caracteristicas': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(),
            'hechos': forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'situacion': forms.NullBooleanSelect(),
        }