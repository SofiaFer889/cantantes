# Generated by Django 4.0.8 on 2022-11-30 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=100, verbose_name='nombre de la empresa')),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artista.artista')),
            ],
        ),
    ]
