# Generated by Django 3.2 on 2021-07-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0005_auto_20210707_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen',
            name='Categoria',
            field=models.CharField(blank=True, choices=[('INTES', 'INTES'), ('URB', 'URB'), ('RUR', 'RUR'), ('ESP', 'ESP'), ('MYE', 'MYE')], max_length=30),
        ),
        migrations.AlterField(
            model_name='examen',
            name='Codigo',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Codigo Certificacion'),
        ),
    ]
