import imghdr
import pyodbc
from PIL import Image
import os,io

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\RegistroNacional\Documents\rnabases\rnapython\Rna.mdb;')
cursor = conn.cursor()
cursor.execute('select Matrícula,Fotografía from registro ')



for row in cursor.columns(table='registro'):
   print (row.column_name) 
   print (row.data_type)
