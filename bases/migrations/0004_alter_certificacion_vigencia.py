# Generated by Django 3.2 on 2022-02-22 16:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0003_certificacion_vigencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificacion',
            name='Vigencia',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
