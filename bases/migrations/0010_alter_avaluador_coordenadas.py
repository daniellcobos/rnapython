# Generated by Django 4.0.4 on 2022-05-05 17:07

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0009_avaluador_coordenadas_alter_certificacion_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaluador',
            name='Coordenadas',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]