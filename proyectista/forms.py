from django import forms
from proyectista.models import Proyectista

class ProyectistaForm(forms.ModelForm):

    class Meta:
        model=Proyectista

        fields = [
            'nombre',
            'dni',
            'direccion',
            'profesion',
            'matricula',
            'tel',
        ]

        labels = {
            'nombre':'Nombre y apellido',
            'dni':'DNI',
            'direccion':'Dirección',
            'profesion':'Profesión',
            'matricula':'N° de Matricula',
            'tel':'Celular',
        }
        CHOISES = (
            ('Maestro/a mayor de obras', 'Maestro/a Mayor de Obras'),
            ('Arquitecto/a', 'Arquitecto/a'),
            ('Ingeniero/a', 'Ingeniero/a'),
        )
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'profesion': forms.Select(choices=CHOISES),
            'matricula': forms.TextInput(attrs={'class':'form-control'}),
            'tel': forms.TextInput(attrs={'class':'form-control'}),
        }

