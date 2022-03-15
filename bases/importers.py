

from pathlib import Path
from datetime import datetime
from .models import *
import pyodbc
from PIL import Image
import io, os
import pandas as pd




def Apellidos(str1,str2):
    surname = " "
    if type(str1) is str and type(str2) is str:
        surname = str1 +' ' + str2
    elif type(str1) is str:
        surname = str1
    else:
        surname = ' '
    return surname

def RNAMat(str1,str2):
    mat = " "
    if type(str1) is str and type(str2) is int:
        mat = str1 +'-' + str(str2)
    elif type(str1) is str:
        mat = str1
    else:
        mat = ' '
    return mat

def NaturalImporter(register):
    registerN = register[register.Nat_o_Jurid == 'N']
    registerN['Fecha_Nacimiento'] = registerN['Fecha_Nacimiento'].fillna(datetime(2100,1,1))
    registerN['Persona_Natural_Apellido_2'] = registerN['Persona_Natural_Apellido_2'].fillna(" ")
    registerN = registerN.fillna("Sin Informacion")

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
            Codinter =  row['Cod_INTER'],
            Pais = row['PAIS'],
            Afiliado =  row['Afiliado'],
            TipoAfiliado =  row['Calidad_de_afiliado'],
            Titulo =  row['Título'],
            Examenes =  row['Exámenes'],
            Tramites =  row['Trámites'],
            Estado =  row['Estado'],
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

def Importer(tipo,register):
    registerU = register[register.Nat_o_Jurid == 'N']
    registerU = registerU.dropna(subset=['Cod_{type}'.format(type = tipo)])
    #fill for Pandas
    registerU = registerU.fillna(datetime(2100,1,1))
    registerU = registerU[[ 'Matrícula','{type}_Otorgamiento'.format(type = tipo), '{type}_Vencimiento'.format(type = tipo),
       '{type}_Renovación'.format(type = tipo), '{type}_Vencimiento_2'.format(type = tipo), 'Cod_{type}'.format(type = tipo)]]
    for index, row in registerU.iterrows():
        Codigorow = row['Cod_{type}'.format(type = tipo)],
        newCert = Certificacion(
            Categoria= '{type}'.format(type = tipo),
            Codigo = Codigorow[0],
            RNA = Avaluador.objects.get(pk = row['Matrícula']),
            Otorgamiento = dateNuller(row['{type}_Otorgamiento'.format(type = tipo)]),
            PrimerVencimiento = dateNuller(row['{type}_Vencimiento'.format(type = tipo)]),
            Renovacion = dateNuller(row['{type}_Renovación'.format(type = tipo)]),
            Vencimiento =dateNuller(row['{type}_Vencimiento_2'.format(type = tipo)])
            )
        
        if not Certificacion.objects.filter(Codigo = Codigorow[0] ).exists():
                newCert.save()
                print(row['Cod_{type}'.format(type = tipo)])
        

def IntImporter(tipo,register):
    print('Cod_{type}'.format(type = tipo))
    registerU = register[register.Nat_o_Jurid == 'N']
    registerU = registerU.dropna(subset=['Cod_{type}'.format(type = tipo)])
    #fill for Pandas
    registerU = registerU.fillna(datetime(2100,1,1))
    registerU = registerU[[ 'Matrícula','{type}_Otorgamiento'.format(type = tipo),
     '{type}_Vencimiento'.format(type = tipo), 'Cod_{type}'.format(type = tipo)]]
    for index, row in registerU.iterrows():
        Codigorow = row['Cod_{type}'.format(type = tipo)],
        newCert = Certificacion(
            Categoria= '{type}'.format(type = tipo),
            Codigo = Codigorow[0],
            RNA = Avaluador.objects.get(pk = row['Matrícula'.format(type = tipo)]),
            Otorgamiento = dateNuller(row['{type}_Otorgamiento'.format(type = tipo)]),
            PrimerVencimiento = dateNuller(row['{type}_Vencimiento'.format(type = tipo)]),
            )
        if not Certificacion.objects.filter(Codigo = Codigorow[0] ).exists():
            newCert.save()
            print(row['Cod_{type}'.format(type = tipo)])

def EmailsImporter(register):
     registerE = register[register.Nat_o_Jurid == 'N']
     registerE = registerE[['Matrícula','E-mail1', 'E-mail2', 'E-mail3']]
     registerE = registerE.fillna("nano")
     for index, row in registerE.iterrows():
         if  Avaluador.objects.filter(pk = row['Matrícula']).exists():
            
            newEmail1 = Email(User = Avaluador.objects.get(pk = row['Matrícula']),EmailString = row['E-mail1'] )
            newEmail2 = Email(User = Avaluador.objects.get(pk = row['Matrícula']),EmailString = row['E-mail2'])
            newEmail3 = Email(User = Avaluador.objects.get(pk = row['Matrícula']),EmailString = row['E-mail3'])
            if not Email.objects.filter(EmailString =  row['E-mail1'] ).exists():
                newEmail1.save()
            if not row['E-mail2'] == "nano" and not Email.objects.filter(EmailString =  row['E-mail2'] ).exists():
                newEmail2.save()
            
            elif not row['E-mail3'] == "nano" and not Email.objects.filter(EmailString =  row['E-mail3'] ).exists():
                newEmail3.save()
               
            

            
def JuridicosImporter(register):
    registerJ = register[register.Nat_o_Jurid == 'J']
    registerJ = registerJ[['NIT','Prefijo','Teléfonos','Fax',
    'Matrícula','Persona_Natural_Apellido_1','Comentarios'
    ,'Persona_Jurídica_Nombre','Representante_Legal_Apellido_1','Representante_Legal_Apellido_2'
    ,'Representante_Legal_Nombres','Celular','Dirección','Consejo_regional'
    ,'Ciudad']]
    for index,row in registerJ.iterrows():
        newPj = PersonaJuridica(
            NIT = row['NIT'],
            MatriculaRNA = RNAMat(row['Prefijo'],row['Matrícula']),
            ConReg=  row['Consejo_regional'],
            Telefono= row['Teléfonos'],
            Fax= row['Fax'],
            Celular= row['Celular'],
            Direccion = row['Dirección'],
            Nombre = row['Persona_Jurídica_Nombre'],
            RepresenanteApellidos = Apellidos(row['Representante_Legal_Apellido_1'],row['Representante_Legal_Apellido_2']),
            RepresenanteNombres = row['Representante_Legal_Nombres'],
            Comentarios = row['Comentarios'],
            )
        print(newPj)
        newPj.save()



def PhotosImporter():
    directory = os.path.dirname(os.path.realpath(__file__))
    list = Avaluador.objects.all()
    for av in list:
        try:
            fullpath = os.path.join(directory,"photos2","{}.bmp".format(av.RNA))
            av.Photo = fullpath
            av.save()
            print(fullpath)
           
        except:
            print("Foto no disponible", av.RNA)

    



 

