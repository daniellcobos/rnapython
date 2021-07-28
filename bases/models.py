from django.db import models

# Create your models here.
class Avaluador(models.Model):
    RNA = models.CharField(primary_key=True,verbose_name = "Codigo RNA (Obligatorio)",max_length=100)
    Identificacion = models.CharField(max_length=100)
    Nombre = models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)
    Year = models.DateField(blank = True, verbose_name = "Fecha de Nacimiento")
    Email1=models.EmailField(blank=True,verbose_name = "Email (Obligatorio)")
    Email2=models.EmailField(blank=True)
    Telefono=models.CharField(blank=True,max_length=100)
    Fax= models.CharField(blank=True,max_length=100)
    Celular=models.CharField(max_length=100, verbose_name = "Telefono Movil (Obligatorio)")
    Direccion = models.CharField(blank=True,max_length=200)
    Ciudad = models.CharField(blank=True,max_length=100)
    ConReg= models.CharField(blank=True,max_length=100)
    Comentarios = models.TextField(blank=True,max_length=1000)
    Codinter = models.CharField(blank=True,max_length=100, verbose_name = "Codigo Internacional")
    Pais = models.CharField(blank=True,max_length=50)
    Afliado = models.BooleanField(verbose_name='Afiliado',default=False)
    Fallecido = models.BooleanField(default=False)
    Suspendido = models.BooleanField(default=False)
    def __str__(self):
        return str(self.Nombre + " "+ self.Apellidos + " ("+ self.RNA+")")
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
    Categoria= models.CharField(blank=True,max_length=30,choices=Categoria_CHOICES)
    Codigo = models.CharField(primary_key=True, verbose_name="Codigo Certificacion",max_length=30)
    RNA = models.ForeignKey(Avaluador,on_delete=models.CASCADE)
    Solicitud = models.DateField(blank=True,null= True )
    Aprobacion = models.DateField(blank=True,null= True )
    Otorgamiento = models.DateField(blank=True, null= True)
    PrimerVencimiento = models.DateField(blank=True )
    Renovacion = models.DateField(blank=True, null= True  )
    Vencimiento = models.DateField(blank=True, null= True )
    def __str__(self):
        return ("Codigo " + str(self.Codigo) + " RNA " + str(self.RNA))
    class Meta:
        verbose_name_plural = "Examenes"
    
