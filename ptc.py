
import pyodbc
from PIL import Image
import io

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT Matrícula,Fotografía FROM Registro')



test = list(cursor)
fotos = []
sinfotos = 0
for i in test:
  try:
    data = i[1][102:]
    data = b'BM H\x0c\x00\x00\x00\x00\x006\x00\x00\x00' + data
    image = Image.open(io.BytesIO(data))
    fotos.append(i[0])
  except:
    if i[1]:
      sinfotos += 1
print(sinfotos)
print(len(fotos))
  



 

