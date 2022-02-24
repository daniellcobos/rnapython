
from ast import Return
from curses.ascii import HT
from re import search, template
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .forms import SearchForm
from . import urls
from .models import *
import io
from xlsxwriter.workbook import Workbook
import xlsxwriter
from datetime import datetime
from .importers import *
from django.db.models.expressions import Window
from django.db.models.functions import RowNumber
from django.db.models import F
from django.views.generic import TemplateView, DetailView
import pandas as pd

def WriteToExcel(request):
    #redo the excel report
    df = pd.DataFrame(list(Avaluador.objects.values()))
    df2 = pd.DataFrame(list(Certificacion.objects.values()))
    print(df)
     
    response = HttpResponse("NADA")
   

    return response

def naturalImporter(request):
    NaturalImporter()
    return  HttpResponse('Importado')

def UrbanImporter(request):
    Importer('URB')
    return  HttpResponse('Importado')

def RuralImporter(request):
    Importer('RUR')
    return  HttpResponse('Importado')

def MaqImporter(request):
    Importer('MYE')
    return  HttpResponse('Importado')

def EspecialesImporter(request):
    Importer('ESP')
    return  HttpResponse('Importado')

def IntUrbanImporter(request):
    IntImporter('INTES_URB')
    return  HttpResponse('Importado')

def IntRuralImporter(request):
    IntImporter('INTES_RUR')
    return  HttpResponse('Importado')

def IntMaqImporter(request):
    IntImporter('INTES_MYE')
    return  HttpResponse('Importado')

def IntEspecialesImporter(request):
    IntImporter('INTES_ESP')
    return  HttpResponse('Importado')

def EmailImporter(requests):
    EmailsImporter()
    return  HttpResponse('Aaaaaa')

def PJimporter(requests):
    JuridicosImporter()
    return  HttpResponse('Aaaaaa')

def Search(request):
    form = SearchForm()
    return render(request, 'Search.html', {'form': form})

def AvaluadorResult(request):
    form = SearchForm()
    if request.method == 'POST':
      
        nombres = request.POST["nombre"]
        apellidos = request.POST["apellidos"]
        Matricula = request.POST['matricula']
        id = request.POST['identificacion']
        if not apellidos and not nombres:
             queryset = Avaluador.objects.filter(Q(RNA=Matricula)|Q(Identificacion=id))
        elif not nombres:
            queryset = Avaluador.objects.filter(Q(RNA=Matricula)|Q(Apellidos__icontains=apellidos))
        elif not apellidos:
            queryset = Avaluador.objects.filter(Q(RNA=Matricula)|Q(Nombre__icontains=nombres))
        elif not Matricula:
             queryset = Avaluador.objects.filter(Q(Nombre__icontains=nombres) & Q(Apellidos__icontains=apellidos)) 
        else:
             queryset = Avaluador.objects.filter(Q(RNA=Matricula)|Q(Nombre__icontains=nombres)|Q(Apellidos__icontains=apellidos)|Q(Identificacion=id))
        results = []
        for q in queryset:
            results.append(q)
        print(results)
        return render(request, 'Searchr.html', {'resultados': results, 'form':form})
    else:
        return render(request, 'Sedarch.html')

def showAvaluador(request,pk):
    FetchedAvaluador = Avaluador.objects.get(RNA=pk)
    avaluadorCerts = Certificacion.objects.filter(RNA=FetchedAvaluador)
    emails = Email.objects.filter(User=FetchedAvaluador)
    certs = []
    emailav = []
    for cert in avaluadorCerts:
        certs.append(cert)
    for email in emails:
        emailav.append(email)
    return render(request, 'Results.html',{'av': FetchedAvaluador, 'certs':certs, 'emails': emailav} )


