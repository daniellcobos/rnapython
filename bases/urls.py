from django.urls import path
from django.conf.urls import url, include
from . import views
app_name='bases'
urlpatterns = [
    path('', views.WriteToExcel,name="reportes"),
]
    