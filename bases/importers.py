import xlrd 

from pathlib import Path
from datetime import datetime
from .models import Avaluador, Examen

excel = Path.cwd() / '2. RNA ONAC JUN 2021.xls'
excelPj = Path.cwd() / 'PersonasJuridicas.xls'
access = str(Path.cwd() / 'LISTADO.xls') 

def dateconverter(dateexcel):
    try:
        año =  xlrd.xldate.xldate_as_datetime(dateexcel,0)
        
        return año
    except:
        stryear = datetime.now()
        return stryear
def dateotorconverter(dateexcel):
    try:
        año =  xlrd.xldate.xldate_as_datetime(dateexcel,0)
        
        return año
    except:
        stryear = ' '
        return stryear

# To open Workbook
def accessExcel():
    avaluadores = []
    certficiaciones = []
    wb = xlrd.open_workbook(access)
    sheet = wb.sheet_by_index(0)
    for i in range(1,sheet.nrows):
        nombre = str(sheet.cell_value(i,12))
        apellido = str(sheet.cell_value(i,10)) +' '+ (str(sheet.cell_value(i,11)))
        id = str(int(sheet.cell_value(i,6)))
        
            
       
        dict = {
            'RNA':id,
            'CC': str(sheet.cell_value(i,14)),
            'Nombre': nombre,
            'Apellido': apellido,
            'ConReg': str(sheet.cell_value(i,4)),
            'Estado': str(sheet.cell_value(i,1)),
            'Email1': str(sheet.cell_value(i,29)),
            'Email2': str(sheet.cell_value(i,30)),
            'Direccion': str(sheet.cell_value(i,32)),
            'Ciudad': str(sheet.cell_value(i,33)),
            'Celular':str(sheet.cell_value(i,36)),
            'Telefono':str(sheet.cell_value(i,34)),
            'Comentarios':str(sheet.cell_value(i,53))
        }
        avaluadores.append(dict)
        urb = {
            'RNA': id,
            'Categoria': 'URB',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,36)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,44)),
            'Codigo': 'URB'+id,
            'Renovacion':  datetime.now(),
            'Vencimiento':  datetime.now(),
        }
        rur = {
            'RNA': id,
            'Categoria': 'RUR',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,9)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,10)),
            'Renovacion':  datetime.now(),
            'Vencimiento':  datetime.now(),
            'Codigo': 'RUR'+id,
        }
        mye = {
            'RNA': id,
            'Categoria': 'MYE',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,14)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,15)),
            'Renovacion': datetime.now(),
            'Vencimiento': datetime.now(),
            'Codigo':'MYE'+id,
        }
        mmo = {
            'RNA':id,
            'Categoria': 'mmo',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,19)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,20)),
            'Renovacion': dateconverter(sheet.cell_value(i,21)),
            'Vencimiento': dateconverter(sheet.cell_value(i,22)),
            'Codigo': 'MMO'+id,
        }
      
        if(sheet.cell_value(i,16)):
            certficiaciones.append(urb)
        if(sheet.cell_value(i,19)):
            certficiaciones.append(rur)
        if(sheet.cell_value(i,22)):
            certficiaciones.append(mye)
        if(sheet.cell_value(i,25)):
            certficiaciones.append(mmo)
  
       
    return [avaluadores,certficiaciones]
def exporter():
    avaluadores = []
    certficiaciones = []
    wb = xlrd.open_workbook(excel)
    sheet = wb.sheet_by_index(2)
    for i in range(1,sheet.nrows):
        nombrec = str(sheet.cell_value(i,2))
        lnombre = nombrec.split()
        separador= ' '
        id = str(int(sheet.cell_value(i,0)))
        
            
        if len(lnombre) > 3:
            nombre = separador.join(lnombre[0:2])
            apellido = separador.join(lnombre[2:])
        else:
            nombre = separador.join(lnombre[0:1])
            apellido = separador.join(lnombre[1:])
        dict = {
            'RNA':id,
            'CC': str(sheet.cell_value(i,1)),
            'Nombre': nombre,
            'Apellido': apellido,
            'Año': dateconverter(sheet.cell_value(i,3)),
            'Codiner': str(sheet.cell_value(i,36)),
            'pais': str(sheet.cell_value(i,37)),
        }
        avaluadores.append(dict)
        urb = {
            'RNA': id,
            'Categoria': 'URB',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,4)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,5)),
            'Renovacion': dateconverter(sheet.cell_value(i,6)),
            'Vencimiento': dateconverter(sheet.cell_value(i,7)),
            'Codigo': str(sheet.cell_value(i,8)),
        }
        rur = {
            'RNA': id,
            'Categoria': 'RUR',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,9)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,10)),
            'Renovacion': dateconverter(sheet.cell_value(i,11)),
            'Vencimiento': dateconverter(sheet.cell_value(i,12)),
            'Codigo': str(sheet.cell_value(i,13)),
        }
        mye = {
            'RNA': id,
            'Categoria': 'MYE',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,14)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,15)),
            'Renovacion': dateconverter(sheet.cell_value(i,16)),
            'Vencimiento': dateconverter(sheet.cell_value(i,17)),
            'Codigo': str(sheet.cell_value(i,18)),
        }
        esp = {
            'RNA':id,
            'Categoria': 'ESP',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,19)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,20)),
            'Renovacion': dateconverter(sheet.cell_value(i,21)),
            'Vencimiento': dateconverter(sheet.cell_value(i,22)),
            'Codigo': str(sheet.cell_value(i,23)),
        }
        intesurb = {
            'RNA':id,
            'Categoria': 'INTES URB',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,24)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,25)),
            'Renovacion': datetime.now(),
            'Vencimiento':  datetime.now(),
            'Codigo': str(sheet.cell_value(i,26)),
        }
        intesrur = {
            'RNA':id,
            'Categoria': 'INTES RUR',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,27)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,28)),
            'Codigo': str(sheet.cell_value(i,29)),
            'Renovacion':  datetime.now(),
            'Vencimiento':  datetime.now(),
        }
        intesmye = {'RNA':id,
            'Categoria': 'INTES MYE',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,30)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,31)),
            'Codigo': str(sheet.cell_value(i,32)),
            'Renovacion':  datetime.now(),
            'Vencimiento':  datetime.now(),
        }
        intesesp = {'RNA':id,
            'Categoria': 'INTES ESP',
            'Otorgacion': dateotorconverter(sheet.cell_value(i,33)),
            'PrimerVencimiento': dateconverter(sheet.cell_value(i,34)),
            'Codigo': str(sheet.cell_value(i,35)),
            'Renovacion':  datetime.now(),
            'Vencimiento':  datetime.now(),
            }
        certficiaciones.append(urb)
        certficiaciones.append(rur)
        certficiaciones.append(mye)
        certficiaciones.append(esp)
        certficiaciones.append(intesurb)
        certficiaciones.append(intesrur)
        certficiaciones.append(intesmye)
        certficiaciones.append(intesesp)
        print(id)
    return [avaluadores,certficiaciones]
    
def PjImporter():
    personasJuridicas = []
    wb = xlrd.open_workbook(access)
    sheet = wb.sheet_by_index(0)
    for i in range(1,sheet.nrows):
     nit = str(sheet.cell_value(i,12))
     nombre = str(sheet.cell_value(i,6))
     represenanteNombres = str(sheet.cell_value(i,11))
     represenanteApellidos = str(sheet.cell_value(i,9)) + str(sheet.cell_value(i,11))
     direccion = str(sheet.cell_value(i,30))
     
     fax = str(sheet.cell_value(i,33))
     celular = str(sheet.cell_value(i,34))
     telefono = str(sheet.cell_value(i,32))
     conReg = str(sheet.cell_value(i,4))
     comentarios = str('nada')
     dict = {
            'NIT':nit,
            'Nombre':nombre,
            'RepresenanteNombres': represenanteNombres,
            'RepresenanteApellidos': represenanteApellidos,
            'Direccion':direccion,
            
            'Celular': celular,
            'Fax': fax,
            'Telefono': telefono,
            'ConReg': conReg,
            'Comentarios': comentarios,
        }
     personasJuridicas.append(dict)
    return personasJuridicas