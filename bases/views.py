
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


def WriteToExcel(request):
    
    output = io.BytesIO()
    workbook = Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    headerf = workbook.add_format(  {'bg_color': '#002206',
    'color': 'white',
    'align': 'center',
    'valign': 'top',
    'border': 1})
    headere = workbook.add_format(  {'bg_color': '#001b44',
    'color': 'white',
    'align': 'center',
    'valign': 'top',
    'border': 1})
    center = workbook.add_format({'align': 'center','valign': 'center',})
    worksheet.set_column('A:E',20)
    worksheet.set_column('F:G',30)
    worksheet.set_column('H:CC',25)
    query = Avaluador.objects.values()
    eheader = list(Certificacion.objects.values().first().keys())
    heads = list(query.first().keys())
    heads = heads[:-3]
   
    columna_inicial = 17
    for n in range(6):
        for i, e in enumerate(eheader):
            worksheet.write(0, columna_inicial, e,headere)
            columna_inicial = columna_inicial + 1
    worksheet.write(0, 16, 'Estado',headerf)
    for i,d in enumerate(heads):
        worksheet.write(0, i, d,headerf)
    for idx, data in enumerate(query):
        estado = ''
        row = 1 + idx
        ldata = list(data.values())
        for i in range(len(data)-3):
            write = ldata[i]
            worksheet.write(row,i,write,center)
        if ldata[16]:
            estado = estado + 'Afiliado '
        if ldata[17]:
            estado = estado + 'Fallecido '
        if ldata[18]:
            estado = estado + 'Suspendido '
        worksheet.write(row,16,estado,center)
        query2= Certificacion.objects.filter(RNA = data['RNA']).values()
        columns = 17
        for q in query2:
            listq = list(q.values())
            for e in listq:
                worksheet.write(row,columns,str(e),center)
                columns = columns+1
        
   
        
    workbook.close()

    output.seek(0)

    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=RNA{}.xlsx".format(datetime.now())
    #response = HttpResponse("NADA")
    output.close()

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

    if request.method == 'POST':
      
        nombres = request.POST["nombre"]
        apellidos = request.POST["apellidos"]
        Matricula = request.POST['matricula']
        if not apellidos and not nombres:
             queryset = Avaluador.objects.filter(Q(RNA=Matricula))
        elif not nombres:
            queryset = Avaluador.objects.filter(Q(RNA=Matricula)|Q(Apellidos__icontains=apellidos))
        elif not apellidos:
            queryset = Avaluador.objects.filter(Q(RNA=Matricula)|Q(Nombre__icontains=nombres))
        elif not Matricula:
             queryset = Avaluador.objects.filter(Q(Nombre__icontains=nombres) & Q(Apellidos__icontains=apellidos)) 
        else:
             queryset = Avaluador.objects.filter(Q(RNA=Matricula)|Q(Nombre__icontains=nombres)|Q(Apellidos__icontains=apellidos))
        results = []
        for q in queryset:
            results.append(q)
        print(results)
        return render(request, 'Searchr.html', {'resultados': results})
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


