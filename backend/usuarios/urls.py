from django.urls import path
from . import views
from usuarios.views_api import lista_usuarios_api, crear_usuario_api

urlpatterns = [

    path('', views.pagina_inicio, name='pagina_inicio'),
    path('usuarios/lista', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo', views.crear_usuario, name='crear_usuario'),
    path('agregar_horas', views.agregar_horas, name='agregar_horas'),
    path('api/usuarios/', lista_usuarios_api, name='lista_usuarios_api'),
    path('api/usuarios/', crear_usuario_api, name='crear_usuario_api'),
]
