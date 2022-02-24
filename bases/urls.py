from django.urls import path
from django.conf.urls import url, include
from . import views
from . views import Search,AvaluadorResult, showAvaluador
app_name='bases'
urlpatterns = [
    path('', views.WriteToExcel,name="reportes"),
    path('naturales', views.naturalImporter,name="Naturales"),
    path('urbanos', views.UrbanImporter,name="Urbanos"),
    path('rurales', views.RuralImporter,name="Rurales"),
    path('maquinaria', views.MaqImporter,name="Maquinaria"),
    path('especiales', views.EspecialesImporter,name="Rurales"),
    path('inturbanos', views.IntUrbanImporter,name="Urbanos"),
    path('intrurales', views.IntRuralImporter,name="Rurales"),
    path('intmaquinaria', views.IntMaqImporter,name="Maquinaria"),
    path('intespeciales', views.IntEspecialesImporter,name="Rurales"),
    path('email', views.EmailImporter,name="email"),
    path('juridicos', views.PJimporter,name="Juridicos"),
    path('buscar', views.Search,name="Busqueda"),
    path('resultados',views.AvaluadorResult, name='search_results'),
    path('avaluador/<int:pk>',views.showAvaluador, name='detailview')
]
    