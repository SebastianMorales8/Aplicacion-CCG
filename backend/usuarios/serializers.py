from rest_framework import serializers
from .models import Usuarios

from rest_framework import serializers
from .models import Usuarios


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'email', 'privilegios', 'telefono1',
                  'telefono2', 'direccion', 'fecha_nacimiento', 'genero']
