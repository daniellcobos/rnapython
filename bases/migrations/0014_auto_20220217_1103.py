# Generated by Django 3.2 on 2022-02-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0013_alter_avaluador_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaluador',
            name='Afiliado',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='avaluador',
            name='Pais',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='avaluador',
            name='TipoAfiliado',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
