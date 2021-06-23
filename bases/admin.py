from django.contrib import admin
from .models import Avaluador, Examen
class Exameninline(admin.TabularInline):
    model = Examen
class AvaluadorAdmin(admin.ModelAdmin):
    search_fields = ('RNA',"Apellidos" )
    inlines = [Exameninline]
class ExamenAdmin(admin.ModelAdmin):
    search_fields = ["Codigo",'RNA__RNA']

# Register your models here.
admin.site.register(Avaluador,AvaluadorAdmin)
admin.site.register(Examen,ExamenAdmin)

