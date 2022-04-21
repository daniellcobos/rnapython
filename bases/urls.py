from django.urls import path

from . import views

app_name='bases'
urlpatterns = [
    path('', views.WriteToExcel,name="reportes"),
    path('buscar', views.Search,name="Busqueda"),
    path('resultados',views.AvaluadorResult, name='search_results'),
    path('avaluador/<int:pk>',views.showAvaluador, name='detailview'),
   
    path('photos',views.phImporter, name='photos'),
    path('vencidos',views.buscarVencidos, name = 'vencidos'),
    path('vigentes',views.SearchVig, name = 'vigentes'),
    path('resultadosvigentes',views.VigResult, name = 'vigentes'),
    path('avaluador', views.AvaluadorList.as_view(), name = 'avaluadores'),
    path('avaluador/api/<int:pk>', views.AvaluadorDetail.as_view(), name = 'avaluadors'),
    path('directorio', views.CertificadoDirectorioList.as_view(), name = 'directorio'),
   
]
    