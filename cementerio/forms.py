from django import forms
from cementerio.models import Cementerio

# Create you forms
class cementerioForm(forms.ModelForm):
    class Meta:
        model = Cementerio

        fields = [
            'fecha_compra',
            'usuario',
            'construccion',
            'lote',
            'lote_num',
            'lote_cuadro',
            'dimension',
            'precio_lote',
            'vigencia',
            'dias_concesion'
            'caduca_concesion',
            'dias_trabajo',
            'abono_anual',
            'contrato',
        ]

        labels = {
            'fecha_compra':'Fecha solicitud',
            'usuario':'Usuario',
            'construccion':'Tipo de construcción',
            'lote':'Lote',
            'lote_num':'Número',
            'lote_cuadro':'Cuadro',
            'dimension':'Dimensión',
            'precio_lote':'Precio',
            'vigencia':'Años del Contrato',
            'dias_concesion':'Plazo en dias para renovación de contratos',
            'dias_trabajo':'Plazo en días para construcción',
            'abono_anual':'Precio del pago Anual',
            'contrato':'Imagen del contrato',
        }
        TIEMPO_CONTRATO = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
        )
        TIPO = (
            ('fosa', 'Fosa'),
            ('nicho', 'Nicho'),
            ('mansuleo', 'Mansuleo'),
        )

        widgets = {
            'fecha_compra': forms.SelectDateWidget(),
            'usuario': forms.Select(attrs={'class':'form-control'}),
            'construccion':forms.Select(choices=TIPO),
            'lote': forms.TextInput(attrs={'class':'form-control'}),
            'lote_num': forms.NumberInput(attrs={'class':'form-control'}),
            'lote_cuadro':forms.TextInput(attrs={'class':'form-control'}),
            'dimension':forms.TextInput(attrs={'class':'form-control'}),
            'precio_lote':forms.NumberInput(attrs={'class':'form-control'}),
            'vigencia':forms.Select(choices=TIEMPO_CONTRATO),
            'dias_concesion':forms.NumberInput(attrs={'class':'form-control'}),
            'dias_trabajo':forms.NumberInput(attrs={'class':'form-control'}),
            'abono_anual':forms.NumberInput(attrs={'class':'form-control'}),
            'contrato': forms.ClearableFileInput(),
        }

class anualForm_1(forms.ModelForm):
    class Meta:
        model = Cementerio

        fields = [
            'monto_anual1',
        ]

        labels = {
            'monto_anual1':'Monto a pagar cuota N°1',
        }

        widgets = {
            'monto_anual1': forms.NumberInput(attrs={'class':'form-control'}),
        }


class anualForm_2(forms.ModelForm):
    class Meta:
        model = Cementerio

        fields = [
            'monto_anual2',
        ]

        labels = {
            'monto_anual2': 'Monto a pagar cuota N°2',
        }

        widgets = {
            'monto_anual2': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class anualForm_3(forms.ModelForm):
    class Meta:
        model = Cementerio

        fields = [
            'monto_anual3',
        ]

        labels = {
            'monto_anual3': 'Monto a pagar cuota N°3',
        }

        widgets = {
            'monto_anual3': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class anualForm_4(forms.ModelForm):
    class Meta:
        model = Cementerio

        fields = [
            'monto_anual4',
        ]

        labels = {
            'monto_anual4': 'Monto a pagar cuota N°4',
        }

        widgets = {
            'monto_anual4': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class permisoForm(forms.ModelForm):
    class Meta:
        model = Cementerio

        fields = [
            'fecha_inicio',
            'metro',
            'precio_metro',
            'prorroga_trabajo',
            # Cambiar estado a True en la vista
        ]

        labels = {
            'fecha_inicio':'Inicio de Construcción',
            'metro':'Metros cuadrados',
            'precio_metro':'Precio por metro cuadrado',
            'prorroga_trabajo':'Dias de prorroga para iniciar trabajos',
        }

        widgets = {
            'fecha_inicio':forms.TextInput(attrs={'class': 'form-control'}),
            'metro':forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_metro':forms.NumberInput(attrs={'class': 'form-control'}),
            'prorroga_trabajo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class fintrabajoForm(forms.ModelForm):
    class Meta:
        model =  Cementerio

        fields = [
            'trabajo_final',
        ]

        labels = {
            'trabajo_final':'Finalizacíon de obra',
        }

        widgets = {
            'trabajo_final':forms.NullBooleanSelect(),
        }