import csv

with open("leer csv/datos.csv") as archivo:
   # print(archivo.read())
   reader = csv.reader(archivo)
   for row in reader:
      print(row)