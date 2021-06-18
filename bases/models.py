from django.db import models

# Create your models here.
class Avaluador(models.Model):
    RNA = models.BigIntegerField(primary_key=True,verbose_name = "Codigo RNA (Obligatorio)")
    Identificacion = models.BigIntegerField(unique=True)
    Nombre = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Year = models.DateField(verbose_name = "Fecha de Nacimiento")
    Email1=models.EmailField(verbose_name = "Email (Obligatorio)")
    Email2=models.EmailField(blank=True)
    Telefono=models.CharField(blank=True,max_length=100)
    Fax= models.CharField(blank=True,max_length=100)
    Celular=models.CharField(max_length=100, verbose_name = "Telefono Movil (Obligatorio)")
    Direccion = models.CharField(blank=True,max_length=100)
    Ciudad = models.CharField(blank=True,max_length=100)
    ConReg= models.CharField(blank=True,max_length=100)
    Afliado = models.BooleanField()
    Fallecido = models.BooleanField()
    Suspendido = models.BooleanField()
    Comentarios = models.TextField(blank=True)
    Codinter = models.CharField(blank=True,max_length=100, verbose_name = "Codigo Internacional")
    Pais = models.CharField(blank=True,max_length=50)
    def __str__(self):
        return str(self.RNA)
    class Meta:
        verbose_name_plural = "Avaluadores"

class Examen(models.Model):
    Categoria_CHOICES = [
    ('INTES', 'INTES'),
    ('URB', 'URB'),
    ('RUR', 'RUR'),
    ('ESP', 'ESP'),
    ('MYE', 'MYE'),
    ]
    Categoria= models.CharField(blank=True,max_length=100,choices=Categoria_CHOICES)
    Codigo = models.BigIntegerField(primary_key=True)
    RNA = models.ForeignKey(Avaluador,on_delete=models.CASCADE)
    Solicitud = models.DateField()
    Aprobacion = models.DateField()
    Otorgamiento = models.DateField()
    PrimerVencimiento = models.DateField()
    Renovacion = models.DateField()
    Vencimiento = models.DateField()
    def __str__(self):
        return ("Codigo " + str(self.Codigo) + " RNA " + str(self.RNA))
    class Meta:
        verbose_name_plural = "Examenes"
    
