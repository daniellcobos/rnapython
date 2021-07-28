from django.shortcuts import render
from django.http import HttpResponse
from . import urls
from .models import *
import io
from xlsxwriter.workbook import Workbook
import xlsxwriter
from datetime import datetime
from .importers import exporter,accessExcel

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
    worksheet.set_column('A:E',20)
    worksheet.set_column('F:G',30)
    worksheet.set_column('H:CC',25)
    query = Avaluador.objects.values()
    eheader = list(Examen.objects.values().first().keys())
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
        query2= Examen.objects.filter(RNA = data['RNA']).values()
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
def testAccess(request):
    data = accessExcel()
    
    for avaluador in data[0][1000:]:
        Avid =avaluador['RNA']
        avAfiliado = False
        avSuspendido = False
        if avaluador['Estado'] == 'vigente':
            avAfiliado = True
        if avaluador['Estado'] == 'Vencido' or avaluador['Estado'] == 'Cancelado':
            avSuspendido = True
        if Avaluador.objects.filter(pk=Avid).exists():
            d = Avaluador.objects.filter(pk=Avid).update(
            Nombre=avaluador['Nombre'],
            Apellidos = avaluador['Apellido'],
            Email1 = avaluador['Email1'],
            Email2 = avaluador['Email2'],
            Telefono = avaluador['Telefono'],
            ConReg = avaluador['ConReg'],
            Afliado = avAfiliado,
            Suspendido = avSuspendido,
            Direccion = avaluador['Direccion'],
            Celular = avaluador['Celular'],
            
            )
            
        else:
            d = Avaluador(
            RNA = Avid,
            Identificacion = avaluador['CC'],
            Nombre=avaluador['Nombre'],
            Apellidos = avaluador['Apellido'],
            Email1 = avaluador['Email1'],
            Email2 = avaluador['Email2'],
            Telefono = avaluador['Telefono'],
            ConReg = avaluador['ConReg'],
            Afliado = avAfiliado,
            Suspendido = avSuspendido,
            Direccion = avaluador['Direccion'],
            Celular = avaluador['Celular'],
    
            Year = datetime.now()
            )
            print(d)
            d.save() 
      
    for examen in data[1]:
        if examen['Otorgacion'] != ' ':
            print(examen)
            e = Examen(
                Codigo = examen['Codigo'],
                RNA = Avaluador.objects.get(RNA = examen['RNA']),
                Categoria = examen['Categoria'],
                Otorgamiento = examen['Otorgacion'],
                PrimerVencimiento =examen['PrimerVencimiento'],
                Renovacion = examen['Renovacion'],
                Vencimiento = examen['Vencimiento'],
            )
            print(e)
            e.save()  
        
    return HttpResponse("Aqui va algo, pero no se que es")
def index(request):
    return HttpResponse("Aqui iba un reporte")

def importer(request):
    data = exporter()
    
    
    for avaluador in data[0]:
       
        d = Avaluador(
        RNA = avaluador['RNA'],
        Identificacion = avaluador['CC'],
        Nombre=avaluador['Nombre'],
        Apellidos = avaluador['Apellido'],
        Year = avaluador['Año'] ,
        Email1 = 'notengo@correo.com',
        Telefono = '1234567890',
        Codinter = avaluador['Codiner'],
        Pais = avaluador['pais'],
        )
        print(d)
        d.save() 
        
    for examen in data[1]:
        if examen['Otorgacion'] != ' ':
            print(examen)
            e = Examen(
                Codigo = examen['Codigo'],
                RNA = Avaluador.objects.get(RNA = examen['RNA']),
                Categoria = examen['Categoria'],
                Otorgamiento = examen['Otorgacion'],
                PrimerVencimiento =examen['PrimerVencimiento'],
                Renovacion = examen['Renovacion'],
                Vencimiento = examen['Vencimiento'],
            )
            print(e)
            e.save()
      
    #print(data)
    response = HttpResponse("NADA")
    
    return response