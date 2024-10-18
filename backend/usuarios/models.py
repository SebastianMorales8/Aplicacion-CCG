from django.db import models


class Usuarios(models.Model):

    nombre = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    privilegios = models.BooleanField(max_length=50)
    grupo = models.IntegerField(choices=[
        (1, 'Grupo 1'),
        (2, 'Grupo 2'),
        (3, 'Grupo 3'),
        (4, 'Grupo 4'),
        (5, 'Grupo 5'),
    ], default=1)
    telefono1 = models.CharField(
        max_length=15, blank=True)  # Teléfono opcional
    telefono2 = models.CharField(
        max_length=15, blank=True)  # Teléfono opcional
    direccion = models.CharField(
        max_length=255, blank=True)  # Dirección opcional
    fecha_nacimiento = models.DateField(
        blank=True, null=True)  # Fecha de nacimiento opcional
    genero = models.CharField(max_length=10, choices=[
        ('M', 'Masculino'),
        ('F', 'Femenino'),

    ], default='M')
    horas_trabajadas = models.IntegerField(default=0)

    def __str__(self):         # pylint: disable=no-member
        return self.nombre


# Create your models here.
