from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

# Create your models here.
class PersonaJuridica(models.Model):
    NIT = models.CharField(primary_key=True,verbose_name = "Codigo RNA (Obligatorio)",max_length=100)
    ConReg= models.CharField(blank=True,max_length=100, verbose_name='Consejo Regional')
    Telefono=models.CharField(blank=True,max_length=100)
    Fax= models.CharField(blank=True,max_length=100)
    Celular=models.CharField(blank=True,max_length=100, verbose_name = "Telefono Movil (Obligatorio)")
    Direccion = models.CharField(blank=True,max_length=200)
    Nombre = models.CharField(max_length=200)
    MatriculaRNA = models.CharField(max_length=50,blank=True)
    RepresenanteApellidos = models.CharField(blank=True,max_length=100)
    RepresenanteNombres = models.CharField(blank=True,max_length=100)
    Comentarios = models.TextField(blank=True,max_length=1000)
    def __str__(self):
        return str(self.Nombre)
class Avaluador(models.Model):
    RNA = models.CharField(primary_key=True,verbose_name = "Codigo RNA (Obligatorio)",max_length=100)
    Identificacion = models.CharField(max_length=100)
    Nombre = models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)
    Photo = models.ImageField(upload_to='photos', null = True, blank = True)
    Year = models.DateField(blank = True, verbose_name = "Fecha de Nacimiento")
    Telefono=models.CharField(blank=True,max_length=100)
    Fax= models.CharField(blank=True,max_length=100)
    Celular=models.CharField(max_length=100, verbose_name = "Telefono Movil (Obligatorio)")
    Direccion = models.CharField(blank=True,max_length=200)
    Ciudad = models.CharField(blank=True,max_length=100)
    ConReg= models.CharField(blank=True,max_length=100, verbose_name='Consejo Regional')
    Comentarios = models.TextField(blank=True,max_length=1000)
    Examenes = models.TextField(blank=True,max_length=1000)
    Tramites = models.TextField(blank=True,max_length=1000)
    Estado = models.TextField(blank=True,max_length=100)
    Codinter = models.CharField(blank=True,max_length=100, verbose_name = "Codigo Internacional")
    Pais = models.CharField(blank=True,max_length=150)
    Afiliado = models.CharField(blank=True,max_length=150)
    TipoAfiliado =  models.CharField(blank=True,max_length=150)
    PersonaJuridica = models.ForeignKey(PersonaJuridica,blank=True,null=True,on_delete=models.SET_NULL)
    Titulo = models.CharField(max_length=150, default= ' ')
    Coordenadas = models.PointField(default=Point(0.0, 0.0))
    def __str__(self):
        return str(self.Nombre + " "+ self.Apellidos)
    class Meta:
        verbose_name_plural = "Avaluadores"

class Certificacion(models.Model):
    Categoria_CHOICES = [
    ('INTES URB', 'INTES URB'),
    ('INTES RUR', 'INTES RUR'),
    ('INTES ESP', 'INTES ESP'),
    ('INTES MYE', 'INTES MYE'),
    ('URB', 'URB'),
    ('RUR', 'RUR'),
    ('ESP', 'ESP'),
    ('MYE', 'MYE'),
    ]
    Categoria= models.CharField(blank=True,max_length=30,choices=Categoria_CHOICES)
    Codigo = models.CharField(unique=True, verbose_name="Codigo Certificacion",max_length=30)
    RNA = models.ForeignKey(Avaluador,on_delete=models.CASCADE, related_name= "Certificacion")
    Otorgamiento = models.DateField(blank=True, null= True)
    PrimerVencimiento = models.DateField(blank=True )
    Renovacion = models.DateField(blank=True, null= True  )
    Vencimiento = models.DateField(blank=True, null= True )
    VigenciaOtorgamiento= models.PositiveIntegerField(blank=True, null= True,  validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='Años de Vigencia Otorgamiento' )
    VigenciaRenovacion= models.PositiveIntegerField(blank=True, null= True,  validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='Años de Vigencia Renovacion' )
    def __str__(self):
        return ("Codigo " + str(self.Codigo) + " RNA " + str(self.RNA))
    class Meta:
        verbose_name_plural = "Certificaciones"
class Email(models.Model):
    EmailString = models.EmailField(max_length=200)
    User = models.ForeignKey(Avaluador,on_delete=models.CASCADE,blank=True, null=True, related_name="Email")
    PJ = models.ForeignKey(PersonaJuridica,on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return(self.EmailString)
