# Generated by Django 3.2 on 2022-02-17 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0011_auto_20210811_1411'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Examen',
            new_name='Certificacion',
        ),
        migrations.AlterModelOptions(
            name='certificacion',
            options={'verbose_name_plural': 'Certifiaciones'},
        ),
        migrations.RemoveField(
            model_name='avaluador',
            name='Afliado',
        ),
        migrations.RemoveField(
            model_name='avaluador',
            name='Email1',
        ),
        migrations.RemoveField(
            model_name='avaluador',
            name='Email2',
        ),
        migrations.RemoveField(
            model_name='avaluador',
            name='Fallecido',
        ),
        migrations.RemoveField(
            model_name='avaluador',
            name='Suspendido',
        ),
        migrations.AddField(
            model_name='avaluador',
            name='Afiliado',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='avaluador',
            name='TipoAfiliado',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='avaluador',
            name='Titulo',
            field=models.CharField(default=' ', max_length=15),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=200)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bases.avaluador')),
            ],
        ),
    ]