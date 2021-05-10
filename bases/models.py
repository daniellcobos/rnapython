from django.db import models

# Create your models here.
class Avaluador(models.Model):
    RNA = models.BigIntegerField(primary_key=True)
    CC = models.BigIntegerField(unique=True)
    Nombre = models.CharField(max_length=100)
    Year = models.SmallIntegerField()
    Email1=models.EmailField()
    Email2=models.EmailField(blank=True)
    Telefono=models.CharField(blank=True,max_length=100)
    Fax= models.CharField(blank=True,max_length=100)
    Celular=models.CharField(blank=True,max_length=100)
    Direccion = models.CharField(blank=True,max_length=100)
    Ciudad = models.CharField(blank=True,max_length=100)
    ConReg= models.CharField(blank=True,max_length=100)
    Afliado = models.BooleanField()
    Comentarios = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = "Avaluadores"

class Examen(models.Model):
    Categoria= models.CharField(blank=True,max_length=100)
    Codigo = models.BigIntegerField(primary_key=True)
    Otorgamiento = models.DateField()
    Renovacion = models.DateField()
    Vencimiento = models.DateField()
    class Meta:
        verbose_name_plural = "Examenes"
    
