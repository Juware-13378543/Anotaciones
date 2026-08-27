
#Abriendo el archivo con with open
with open("archivos/texto.txt",encoding="UTF-8") as archivo:

    #leemos el archivo
    contenido = archivo.read()

    #Mostramos el archivo
    print(contenido)