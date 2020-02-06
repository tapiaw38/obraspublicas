from django import forms
from usuario.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario

        fields = [
            'nombre',
            'dni',
            'direccion',
            'catastro',
            'tel',
        ]

        labels = {
            'nombre':'Nombre y apellido',
            'dni':'DNI',
            'direccion':'Dirección',
            'catastro':'Matricula Catastral',
            'tel':'Celular',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'catastro': forms.TextInput(attrs={'class':'form-control'}),
            'tel': forms.TextInput(attrs={'class':'form-control'}),
        }