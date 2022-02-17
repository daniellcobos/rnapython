import xlrd 

from pathlib import Path
from datetime import datetime
from .models import *

import pandas as pd

register = pd.read_excel(r'C:\Users\RegistroNacional\Documents\rnabases\rnapython\c.xlsx')
register.columns = [c.replace(' ', '_') for c in register.columns]

def Apellidos(str1,str2):
    surname = " "
    if type(str1) is str and type(str2) is str:
        surname = str1 +' ' + str2
    elif type(str1) is str:
        surname = str1
    else:
        surname = ' '
    return surname

def NaturalImporter(): 
    registerN = register[register.Nat_o_Jurid == 'N']
    registerN = registerN.fillna(datetime(1900,1,1))
    for index, row in registerN.iterrows():
        newAvaluador = Avaluador(
            RNA = row['Matrícula'],
            Identificacion = row['NIT'],
            Nombre = row['Persona_Natural_Nombres'],
            Apellidos =  Apellidos(row['Persona_Natural_Apellido_1'],row['Persona_Natural_Apellido_2']),
            Year =  row['Fecha_Nacimiento'],
            Telefono= row['Teléfonos'],
            Fax= row['Fax'],
            Celular= row['Celular'],
            Direccion =  row['Dirección'],
            Ciudad =  row['Ciudad'],
            ConReg=  row['Consejo_regional'],
            Comentarios =  row['Comentarios'],
            Codinter =  row['Persona_Natural_Nombres'],
            Pais = row['PAIS'],
            Afiliado =  row['Afiliado'],
            TipoAfiliado =  row['Calidad_de_afiliado'],
            Titulo =  row['Título'],
        ) 
        if not Avaluador.objects.filter(pk = row['Matrícula']).exists():
            print( Apellidos(row['Persona_Natural_Apellido_1'],row['Persona_Natural_Apellido_2']))
            newAvaluador.save()
        else:
            print( Apellidos(row['Persona_Natural_Apellido_1'],row['Persona_Natural_Apellido_2']))

def dateNuller(date):
    fillerdate = datetime(2100,1,1)
    if date == fillerdate:
        return None
    else:
        return date

def Importer(tipo):
    registerU = register[register.Nat_o_Jurid == 'N']
    registerU = registerU.dropna(subset=['Cod_{type}'.format(type = tipo)])
    #fill for Pandas
    registerU = registerU.fillna(datetime(2100,1,1))
    registerU = registerU[[ 'Matrícula','{type}_Otorgamiento'.format(type = tipo), '{type}_Vencimiento'.format(type = tipo),
       '{type}_Renovación'.format(type = tipo), '{type}_Vencimiento_2'.format(type = tipo), 'Cod_{type}'.format(type = tipo)]]
    for index, row in registerU.iterrows():
        newCert = Certificacion(
            Categoria= '{type}'.format(type = tipo),
            Codigo = row['Cod_{type}'.format(type = tipo)],
            RNA = Avaluador.objects.get(pk = row['Matrícula'.format(type = tipo)]),
            Otorgamiento = dateNuller(row['{type}_Otorgamiento'.format(type = tipo)]),
            PrimerVencimiento = dateNuller(row['{type}_Vencimiento'.format(type = tipo)]),
            Renovacion = dateNuller(row['{type}_Renovación'.format(type = tipo)]),
            Vencimiento =dateNuller(row['{type}_Vencimiento_2'.format(type = tipo)])
            )
        if Avaluador.objects.filter(pk = row['Matrícula']).exists():
            newCert.save()
            print(row['Cod_{type}'.format(type = tipo)])


