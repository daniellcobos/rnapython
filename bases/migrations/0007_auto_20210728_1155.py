# Generated by Django 3.2 on 2021-07-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0006_auto_20210707_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaluador',
            name='Email1',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email (Obligatorio)'),
        ),
        migrations.AlterField(
            model_name='avaluador',
            name='Year',
            field=models.DateField(blank=True, verbose_name='Fecha de Nacimiento'),
        ),
    ]