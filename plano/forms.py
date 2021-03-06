from django import forms
from plano.models import Plano
from usuario.models import Usuario

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano

        fields = [
            'fecha',
            'usuario',
            'proyectista',
            'dir_obra',
            'precio_metro',
            'metros',
            'cuota',
        ]

        labels = {
            'fecha':'Fecha de solicitud',
            'usuario': 'Usuario',
            'proyectista':'Proyectista',
            'dir_obra': 'Dirección de la obra',
            'precio_metro': 'Precio por metro cuadrado',
            'metros': 'Metros totales del plano',
            'cuota': 'Pago en cuotas',
        }

        CHOISES = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
        )

        widgets = {
            'fecha': forms.SelectDateWidget(),
            'usuario': forms.Select(attrs={'class':'form-control'}),
            'proyectista':forms.Select(attrs={'class':'form-control'}),
            'dir_obra': forms.TextInput(attrs={'class':'form-control'}),
            'precio_metro': forms.TextInput(attrs={'class':'form-control'}),
            'metros':forms.TextInput(attrs={'class':'form-control'}),
            'cuota':forms.Select(choices=CHOISES),
        }

class DeudaForm(forms.ModelForm):
    class Meta:
        model = Plano

        fields = [
            'pago',
            'fecha_pago',
        ]

        labels = {
            'pago':'Total abonado',
            'fecha_pago':'Fecha de pago',
        }

        widgets = {
            'pago' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_pago' : forms.SelectDateWidget(),
        }

class DeudaForm2(forms.ModelForm):
    class Meta:
        model = Plano

        fields = [
            'pago2',
            'fecha_pago2',
        ]

        labels = {
            'pago2':'Total abonado',
            'fecha_pago2':'Fecha de pago cuota 2',
        }

        widgets = {
            'pago2' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_pago2' : forms.SelectDateWidget(),
        }

class DeudaForm3(forms.ModelForm):
    class Meta:
        model = Plano

        fields = [
            'pago3',
            'fecha_pago3',
        ]

        labels = {
            'pago3':'Total abonado',
            'fecha_pago3':'Fecha de pago cuota 3',
        }

        widgets = {
            'pago3' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_pago3' : forms.SelectDateWidget(),
        }

class DeudaForm4(forms.ModelForm):
    class Meta:
        model = Plano

        fields = [
            'pago4',
            'fecha_pago4',
        ]

        labels = {
            'pago4':'Total abonado',
            'fecha_pago4':'Fecha de pago cuota 4',
        }

        widgets = {
            'pago4' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_pago4' : forms.SelectDateWidget(),
        }