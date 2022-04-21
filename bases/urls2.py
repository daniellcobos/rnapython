from django.urls import path

from . import views
from . views import Search,AvaluadorResult, showAvaluador
app_name='bases'
urlpatterns = [
    path('', views.WriteToExcel,name="reportes"),
    path('subirarchivo',views.subirArchivo, name='subirArchivo'),
    path('leerarchivo',views.leerArchivo, name='leerArchivo'),
    path('photos',views.phImporter, name='photos'),
    path('leerarchivoONAC',views.leerArchivoONAC, name='leerArchivoOnac')
]
    