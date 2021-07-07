# Generated by Django 3.2 on 2021-07-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0004_auto_20210707_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen',
            name='Aprobacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='Otorgamiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='PrimerVencimiento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='Renovacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='Solicitud',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='Vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
