from django.contrib import admin
from .models import *
from .forms import *


class Certificacioninline(admin.TabularInline):
    model = Certificacion
    
class Certificacioncreateinline(admin.TabularInline):
    model = Certificacion
    form = CertificacionCreateForm
class Emailinline(admin.TabularInline):
    model = Email
class AvaluadorAdmin(admin.ModelAdmin):
    search_fields = ('RNA',"Apellidos" )
    inlines = [Certificacioninline,Certificacioncreateinline,Emailinline]

class CertificacionAdmin(admin.ModelAdmin):
    search_fields = ["Codigo",'RNA__RNA']
    form = CertificacionCreateForm
# Register your models here.
admin.site.register(Avaluador,AvaluadorAdmin)
admin.site.register(Certificacion,CertificacionAdmin)
admin.site.register(PersonaJuridica)

