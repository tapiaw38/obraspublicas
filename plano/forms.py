from django import forms
from plano.models import Plano
from usuario.models import Usuario

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano

        fiels = [
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
            'usuario': forms.ModelChoiceField(attrs={'class':'form-control'}),
            'dir_obra': forms.TextInput(attrs={'class':'form-control'}),
            'precio_metro': forms.IntegerField(attrs={'class':'form-control'}),
            'metros':forms.IntegerField(attrs={'class':'form-control'}),
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
            'total' : forms.IntegerField(attrs={'class':'form-control'}),
            'pago' : forms.IntegerField(attrs={'class':'form-control'}),
            'fecha_pago' : forms.DateField(attrs={'class':'form-control'}),
            'deuda' : forms.IntegerField(attrs={'class':'form-control'}),
        }