
from ast import Return
from curses.ascii import HT
from re import search, template
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .forms import SearchForm, SearchVigForm
from . import urls
from .models import *
import io
from xlsxwriter.workbook import Workbook
from django.contrib.auth.decorators import login_required

from datetime import datetime, date, timedelta
from .importers import *
from django.db.models.expressions import Window
from django.db.models.functions import RowNumber
from django.db.models import F
from django.views.generic import TemplateView, DetailView
import pandas as pd
from .serializers import *
from rest_framework import generics

def WriteToExcel(request):
    #redo the excel report
    writer = pd.ExcelWriter(r'Reporte.xlsx', engine='xlsxwriter')
    df = pd.DataFrame(list(Avaluador.objects.values()))
    df = df.drop('Photo', axis=1)
    df2 = pd.DataFrame(list(Certificacion.objects.values()))
    df2 = df2.groupby("RNA_id")
    for i in range(1,9):
            df["Categoria_{}".format(i)] = ""
            df["Codigo_{}".format(i)] = ""
            df["Otorgamiento_{}".format(i)] =""
            df["PrimerVencimiento_{}".format(i)] = ""
            df["Renovacion_{}".format(i)] =""
            df["Vencimiento_{}".format(i)] = ""
    for id in df['RNA']:
       
        index = df[df['RNA'] == id].index.item()
        try:
            certdf = df2.get_group(id)
            rows = 1
            for item,row in certdf.iterrows():
                print(df.iloc[index])
                df.iloc[index, df.columns.get_loc("Categoria_{}".format(rows))] = row['Categoria']
                df.iloc[index, df.columns.get_loc("Codigo_{}".format(rows))] = row['Codigo']
                df.iloc[index, df.columns.get_loc("Otorgamiento_{}".format(rows))] =row['Otorgamiento']
                df.iloc[index, df.columns.get_loc("PrimerVencimiento_{}".format(rows))] = row['PrimerVencimiento']
                df.iloc[index, df.columns.get_loc("Renovacion_{}".format(rows))] =row['Renovacion']
                df.iloc[index, df.columns.get_loc("Vencimiento_{}".format(rows))] = row['Vencimiento']
                rows += 1                 
        except:
            print(id)
    df.to_excel(writer, sheet_name='reporte',index=False)
   
    worksheet = writer.sheets['reporte']
    data_format1 = writer.book.add_format({'bg_color': '#60A84D'})
    worksheet.set_row(0,cell_format=data_format1)
    worksheet.set_column("A:BR",25)
    worksheet.autofilter(0, 0, df.shape[0], df.shape[1] - 1)
    writer.save()
    



    with open(r'Reporte.xlsx', 'rb') as fh:
     response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
     response['Content-Disposition'] = "attachment; filename=RNA{}.xlsx".format(datetime.now())
     return response
    
@login_required
def Search(request):
    form = SearchForm()
    return render(request, 'Search.html', {'form': form})

@login_required
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

@login_required
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

@login_required
def showCertificacion(request,pk):
    FetchedCertificacion = Certificacion.objects.get(Codigo=pk)
    return render(request, 'CertResults.html',{'certs': FetchedCertificacion } )

@login_required
def subirArchivo(request):
    return render(request, 'Importer.html' )

@login_required
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
        except Exception as e :
            print(e)
            return render(request,'error.html', {'e':e})

def leerArchivoONAC(request):
    if request.method == 'POST':
            file = request.FILES['import']
            register = pd.read_excel(file,engine='openpyxl',sheet_name='CERTIFICADOS ONAC')
            register.columns = [c.replace('\n', '_') for c in register.columns]
            register.columns = [c.replace(' ', '_') for c in register.columns]
            ONACImporter(register)
            print(register.columns)
            return render(request, 'Importer.html' )
       

def phImporter(request):
    PhotosImporter()
    return HttpResponse('Fotos Importadas')

@login_required
def buscarVencidos(request):
    nextmonth = date.today() + timedelta(days=30)
    list = Certificacion.objects.filter(Vencimiento__lte = nextmonth).filter(Vencimiento__gte = date.today() )
    list2 = Certificacion.objects.filter(PrimerVencimiento__lte = nextmonth).filter(PrimerVencimiento__gte = date.today() )
    avList = []
    for l in list:
        avList.append(l.RNA)
    for l in list2:
        avList.append(l.RNA)
    return render(request, 'vencidos.html', {'avaluadores' : avList} )


@login_required
def SearchVig(request):
    form = SearchVigForm()
    return render(request, 'SearchVig.html', {'form': form})


@login_required
def VigResult(request):
    avList = []
    if request.method == 'POST':
        vigente = request.POST["Vigente"]
        categoria = request.POST["Categoria"]
        
        print(vigente)
        if vigente == 'Vigentes':
            certs1 = Certificacion.objects.filter(Q(Vencimiento__gte = date.today())|Q(PrimerVencimiento__gte =date.today() )).filter(Categoria = categoria).distinct()
            for l in certs1:
                avList.append(l.RNA)
        elif vigente == 'Vencidos':
           certs1 = Certificacion.objects.filter(Q(Vencimiento__lte = date.today())|Q(PrimerVencimiento__lte =date.today() )).filter(Categoria = categoria).distinct()
           for l in certs1:
                avList.append(l.RNA)
        return render(request, 'vigentes.html', {'avaluadores' : avList, 'vigente' : vigente, 'categoria' : categoria} )
    else:
        return HttpResponse("Mas Nada")

class AvaluadorList(generics.ListAPIView):
    queryset = Avaluador.objects.all()
    serializer_class = AvaluadorListSerializer

class AvaluadorDetail(generics.RetrieveAPIView):
     queryset = Avaluador.objects.all()
     serializer_class = AvaluadorDetailSerializer

class CertificadoDirectorioList(generics.ListAPIView):
    queryset =Certificacion.objects.filter(Q(Vencimiento__gte = date.today())|Q(PrimerVencimiento__gte =date.today() ))
    serializer_class = CertificacionDirectorioSerializer