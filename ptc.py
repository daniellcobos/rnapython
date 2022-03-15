
import pyodbc
from PIL import Image
import io,os

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT Matrícula,Fotografía FROM Registro')
directory = os.path.dirname(os.path.realpath(__file__))


test = list(cursor)
fotos = 0
sinfotos = 0
for i in test:
  try:
      print("compatible")
      fullpath = os.path.join(directory, "{}.bmp".format(i[0]))
      data = i[1][102:]
      data = b'BM H\x0c\x00\x00\x00\x00\x006\x00\x00\x00' + data
      img = Image.open(io.BytesIO(data))
      fotos += 1
      img.save(fullpath)
    
  except:
    if i[1]:
      print("No compatible")
      sinfotos += 1
print(sinfotos)
print(fotos)
  



 

