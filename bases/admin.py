from django.contrib import admin
from .models import Avaluador, Examen

class AvaluadorAdmin(admin.ModelAdmin):
    search_fields = ('RNA',"Apellidos" )

# Register your models here.
admin.site.register(Avaluador,AvaluadorAdmin)
admin.site.register(Examen)

