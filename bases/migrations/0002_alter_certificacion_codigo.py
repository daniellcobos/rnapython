# Generated by Django 3.2 on 2022-02-22 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificacion',
            name='Codigo',
            field=models.CharField(max_length=30, unique=True, verbose_name='Codigo Certificacion'),
        ),
    ]
