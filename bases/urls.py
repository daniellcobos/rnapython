from django.urls import path
from django.conf.urls import url, include
from . import views
app_name='bases'
urlpatterns = [
    path('', views.WriteToExcel,name="reportes"),
    path('import',views.importer,name= 'importer'),
    path('access',views.testAccess,name= 'access'),
    path('pj',views.Pjimporter,name= 'access'),
]
    