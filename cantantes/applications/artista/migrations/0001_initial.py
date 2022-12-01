# Generated by Django 4.0.8 on 2022-11-30 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido')),
                ('foto', models.ImageField(upload_to='')),
                ('dni', models.PositiveIntegerField()),
                ('fecha_de_nacimiento', models.DateField()),
                ('sueldo_mensual', models.PositiveIntegerField()),
            ],
        ),
    ]
