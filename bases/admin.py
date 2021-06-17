from django.contrib import admin
from .models import Avaluador, Examen

class AvaluadorAdmin(admin.ModelAdmin):
    search_fields = ('RNA',"Apellidos" )
class ExamenAdmin(admin.ModelAdmin):
    search_fields = ["Codigo"]
# Register your models here.
admin.site.register(Avaluador,AvaluadorAdmin)
admin.site.register(Examen,ExamenAdmin)

