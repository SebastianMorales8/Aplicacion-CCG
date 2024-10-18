from django.shortcuts import render, redirect
from .models import Usuarios
from .forms import UsuarioForm, HorasForm


def pagina_inicio(request):
    return render(request, 'usuarios/pagina_inicio.html')


def lista_usuarios(request):
    usuarios = Usuarios.objects.all()  # pylint: disable=no-member
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()

    return render(request, 'usuarios/crear_usuario.html', {'form': form})


def agregar_horas(request):
    if request.method == 'POST':
        form = HorasForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            horas = form.cleaned_data['horas']
            usuario.horas_trabajadas += horas
            usuario.save()
            return redirect('pagina_inicio')
    else:
        form = HorasForm()

    return render(request, 'usuarios/agregar_horas.html', {'form': form})
