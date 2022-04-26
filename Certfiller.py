from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import os

path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"static","plantillas","Plantilla_Certificados_Urbanos V8 NTS.docx")
template = path

document = MailMerge(template)
print(document.get_merge_fields())
document.merge(
Codigo = "AAAAAAAA",
Vencimiento = 'Arrrr',
Nombre = 'Me',
Rna = 'Spongebob',
Cedula = 'Me boooi',
Renovacion = "Do",
Actualizacion ="Me Some",
Otorgamiento = "Cangreburgers"
)


document.write('test-output.docx')