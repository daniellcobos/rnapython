from django.contrib import admin
from .models import *
class Exameninline(admin.TabularInline):
    model = Certificacion
class AvaluadorAdmin(admin.ModelAdmin):
    search_fields = ('RNA',"Apellidos" )
    inlines = [Exameninline]
class CertificacionAdmin(admin.ModelAdmin):
    search_fields = ["Codigo",'RNA__RNA']

# Register your models here.
admin.site.register(Avaluador,AvaluadorAdmin)
admin.site.register(Certificacion,CertificacionAdmin)
admin.site.register(PersonaJuridica)

