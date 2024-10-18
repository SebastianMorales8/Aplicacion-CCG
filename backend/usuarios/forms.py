from django import forms
from .models import Usuarios


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'email', 'privilegios', 'telefono1',
                  'telefono2', 'direccion', 'fecha_nacimiento', 'genero']
        widgets = {
            # Para un selector de fecha
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }


class HorasForm(forms.Form):
    usuario = forms.ModelChoiceField(
        queryset=Usuarios.objects.all())   # pylint: disable=no-member
    horas = forms.IntegerField(label='horas trabajadas')
