from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import os


def Merger(cert,av):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"static","plantillas","Plantilla_{}.docx".format(cert.Categoria))
    template = path

    document = MailMerge(template)
    cCodigo = cert.Codigo
    
    cNombre = av.Nombre +" " +av.Apellidos
    cRna = cert.RNA.RNA
    cCedula = av.Identificacion
    if cert.Renovacion:
        cRenovacion = cert.Renovacion
    else:
        cRenovacion = "-"
    if cert.Vencimiento:
        cVencimiento = cert.Vencimiento
    else:
        cVencimiento = "-"
    cActualizacion = cert.PrimerVencimiento
    cOtorgamiento = cert.Otorgamiento

    document.merge(
    Codigo = cCodigo,
    Vencimiento =str(cVencimiento),
    Nombre = cNombre,
    Rna = cRna,
    Cedula = str(cCedula),
    Renovacion = str(cRenovacion),
    Actualizacion = str(cActualizacion),
    Otorgamiento = str(cOtorgamiento),
    )
    return document
    
