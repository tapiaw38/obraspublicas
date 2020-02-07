from django import forms
from plano.models import Plano
from usuario.models import Usuario

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano

        fields = [
            'fecha',
            'usuario',
            'dir_obra',
            'precio_metro',
            'metros',
        ]

        labels = {
            'fecha':'Fecha de solicitud',
            'usuario': 'Usuario',
            'dir_obra': 'Dirección de la obra',
            'precio_metro': 'Precio por metro cuadrado',
            'metros': 'Metros totales del plano',
        }

        widgets = {
            'fecha': forms.SelectDateWidget(),
            'usuario': forms.Select(attrs={'class':'form-control'}),
            'dir_obra': forms.TextInput(attrs={'class':'form-control'}),
            'precio_metro': forms.TextInput(attrs={'class':'form-control'}),
            'metros':forms.TextInput(attrs={'class':'form-control'}),
        }

class DeudaForm(forms.ModelForm):
    class Meta:
        model = Plano

        fields = [
            'total',
            'pago',
            'fecha_pago',
            'deuda',
        ]

        labels = {
            'total':'Total a pagar',
            'pago':'Total abonado',
            'fecha_pago':'Fecha de pago',
            'deuda': 'Deuda',
        }

        widgets = {
            'total' : forms.TextInput(attrs={'class':'form-control'}),
            'pago' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_pago' : forms.SelectDateWidget(),
            'deuda' : forms.TextInput(attrs={'class':'form-control'}),
        }