from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuarios
# pylint: disable=no-name-in-module
from .serializers import UsuarioSerializer


@api_view(['GET', 'POST'])
def lista_usuarios_api(request):
    if request.method == 'GET':
        usuarios = Usuarios.objects.all()       # pylint: disable=no-member
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def agregar_horas_api(request):
    if request.method == 'POST':
        usuario_id = request.data.get('usuario')
        horas = request.data.get('horas')

        try:
            usuario = Usuarios.objects.get(           # pylint: disable=no-member
                id=usuario_id)   # pylint: disable=no-member
            # Asegúrate de que este campo exista en tu modelo
            usuario.horas_trabajadas += horas
            usuario.save()
            return Response(UsuarioSerializer(usuario).data, status=status.HTTP_200_OK)
        except Usuarios.DoesNotExist:                      # pylint: disable=no-member
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT', 'DELETE'])
def usuario_detalle(request, id):
    try:
        usuario = Usuarios.objects.get(id=id)       # pylint: disable=no-member
    except Usuarios.DoesNotExist:                   # pylint: disable=no-member
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
