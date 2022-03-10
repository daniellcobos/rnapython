
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
from datetime import datetime, date
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
    df1 = df.to_excel()
    print(df)
     
    response = HttpResponse("NADA")
   

    return response

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
        if not apellidos and not nombres and not Matricula:
             queryset = Avaluador.objects.filter(Q(Identificacion__icontains=id))
        elif not apellidos and not nombres:
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
    today = date.today()
    avaluadorCerts = Certificacion.objects.filter(RNA=FetchedAvaluador)
    emails = Email.objects.filter(User=FetchedAvaluador)
    certs = []
    emailav = []
    for cert in avaluadorCerts:
        certs.append(cert)
    for email in emails:
        emailav.append(email)
    
    return render(request, 'Results.html',{'av': FetchedAvaluador, 'certs':certs, 'emails': emailav, 'today': today} )

def subirArchivo(request):
    return render(request, 'Importer.html' )


def leerArchivo(request):
    if request.method == 'POST':
        try:
            file = request.FILES['import']
            register = pd.read_excel(file,engine='openpyxl')
            register.columns = [c.replace(' ', '_') for c in register.columns]
            NaturalImporter(register)
            JuridicosImporter(register)
            EmailsImporter(register)
            categorias = ['URB','RUR','ESP','MYE']
            for cat in categorias:
                Importer(cat,register)
            for cat in categorias:
                Intcat = "INTES_" + cat
                IntImporter(Intcat,register)
            return render(request, 'Importer.html' )
        except:
            return HttpResponse('Subiste el archivo equivocao')


def phImporter(request):
    PhotosImporter()
    return HttpResponse('Fotos Importadas')