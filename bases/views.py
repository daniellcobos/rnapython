from django.shortcuts import render
from django.http import HttpResponse
from . import urls
from .models import *
import io
from xlsxwriter.workbook import Workbook
import xlsxwriter
from datetime import datetime

def WriteToExcel(weather_data, town=None):
    
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
    worksheet.set_column('A:E',15)
    worksheet.set_column('F:G',25)
    worksheet.set_column('H:CC',20)
    query = Avaluador.objects.values()
    eheader = Examen.objects.values().first().keys()
    heads = query.first().keys()
    
    columna_inicial = 19
    for n in range(6):
        for i, e in enumerate(eheader):
            worksheet.write(0, columna_inicial, e,headere)
            columna_inicial = columna_inicial + 1
    for i,d in enumerate(heads):
        worksheet.write(0, i, d,headerf)
    for idx, data in enumerate(query):
        row = 1 + idx
        ldata = list(data.values())
        for i in range(len(data)):
            write = ldata[i]
            
            if write == False:
               write = "No"
            if  write == True:
                write = "Si"
            worksheet.write(row,i,write,center)
        query2= Examen.objects.filter(RNA = data['RNA']).values()
        columns = 19
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

def index(request):
    return HttpResponse("Aqui iba un reporte")