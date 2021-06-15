from django.shortcuts import render
from django.http import HttpResponse
from . import urls
from .models import *
import io
from xlsxwriter.workbook import Workbook
import xlsxwriter


def WriteToExcel(weather_data, town=None):
    headers = ['Codigo','RNA','Nombre','Apellidos','Identificacion','Fecha de Nacimiento',"Email",'Categoria','Solicitud','Aprobacion','Vencimento','Otorgamiento','Primer Vencimiento']
    output = io.BytesIO()
    workbook = Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    headerf = workbook.add_format(  {'bg_color': '#F7F7F7',
    'color': 'black',
    'align': 'center',
    'valign': 'top',
    'border': 1})
    center = workbook.add_format({'align': 'center','valign': 'center',})
    worksheet.set_column('A:E',15)
    worksheet.set_column('F:G',25)
    worksheet.set_column('H:Z',20)
    query = Examen.objects.all()
    for i,head in enumerate(headers):
        worksheet.write_string(0,i,head,headerf)
    for idx, data in enumerate(query):
        row = 1 + idx
        Codigo = str(data.Codigo)
        rna = str(data.RNA_id)
        examinado = Avaluador.objects.get(pk=rna)
        id = str(examinado.Identificacion)
        worksheet.write_string(row, 0, Codigo,center)
        worksheet.write_string(row, 1, rna,center)
        worksheet.write(row, 2, examinado.Nombre)
        worksheet.write(row, 3, examinado.Apellidos)
        worksheet.write(row, 4, id,center)
        worksheet.write(row, 5, examinado.Year.strftime('%d/%m/%Y'))
        worksheet.write(row, 6, examinado.Email1)
        worksheet.write_string(row, 7, data.Categoria)
        worksheet.write(row, 8, data.Solicitud.strftime('%d/%m/%Y'),center)
        worksheet.write(row, 10, data.Vencimiento.strftime('%d/%m/%Y'),center)
        worksheet.write(row, 9, data.Aprobacion.strftime('%d/%m/%Y'),center)
        worksheet.write(row, 11, data.Otorgamiento.strftime('%d/%m/%Y'),center)
        worksheet.write(row, 12, data.PrimerVencimiento.strftime('%d/%m/%Y'),center)
        
    workbook.close()

    output.seek(0)

    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=test.xlsx"

    output.close()

    return response

def index(request):
    return HttpResponse("Aqui iba un reporte")