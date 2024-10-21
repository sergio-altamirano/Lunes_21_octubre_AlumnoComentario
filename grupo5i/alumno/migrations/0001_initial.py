# Generated by Django 5.1.1 on 2024-10-15 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apaterno', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('Amaterno', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('fecha_nacimiento', models.DateField(verbose_name='fecha de nacimiento')),
                ('fecha_ingreso', models.DateField(verbose_name='fecha de ingreso')),
            ],
        ),
        migrations.CreateModel(
            name='Frase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=400, verbose_name='comentario')),
                ('Alumnos_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumno.alumno')),
            ],
        ),
    ]