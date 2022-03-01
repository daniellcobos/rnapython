# Generated by Django 3.2 on 2022-02-24 16:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0004_alter_certificacion_vigencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaluador',
            name='Estado',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='avaluador',
            name='Examenes',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='avaluador',
            name='Tramites',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='certificacion',
            name='Vigencia',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Años de Vigencia'),
        ),
    ]