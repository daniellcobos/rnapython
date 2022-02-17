from django.contrib import admin
from .models import *
class Certificacioninline(admin.TabularInline):
    model = Certificacion
class Emailinline(admin.TabularInline):
    model = Email
class AvaluadorAdmin(admin.ModelAdmin):
    search_fields = ('RNA',"Apellidos" )
    inlines = [Certificacioninline,Emailinline]

class CertificacionAdmin(admin.ModelAdmin):
    search_fields = ["Codigo",'RNA__RNA']

# Register your models here.
admin.site.register(Avaluador,AvaluadorAdmin)
admin.site.register(Certificacion,CertificacionAdmin)
admin.site.register(PersonaJuridica)

