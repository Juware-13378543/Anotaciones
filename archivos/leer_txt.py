archivo_sin_leer = open("archivos/texto.txt",encoding="UTF-8")

#Leer archivo completo
#archivo = archivo_sin_leer.read()

#leer linea por linea
#linea_1= archivo_sin_leer.readlines()

#Leer una sola linea
linea = archivo_sin_leer.readlines(100)


#Cerrar el archivo
archivo_sin_leer.close()

print(linea)
