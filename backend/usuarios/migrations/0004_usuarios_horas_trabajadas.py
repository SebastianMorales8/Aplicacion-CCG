# Generated by Django 5.1.2 on 2024-10-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_usuarios_direccion_usuarios_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='horas_trabajadas',
            field=models.IntegerField(default=0),
        ),
    ]