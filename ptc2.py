import base64
import imghdr
import pyodbc
from PIL import Image
import os,io

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT Matrícula,Fotografía FROM Registro')



test = list(cursor)
tester = test[998]
print(tester[0])

data = tester[1][0:200]
image = print(data)
print('\n')



with open("test.bmp", "rb") as image:
  f = image.read()

  b = bytes(f)
#print(b[0:60]) 
