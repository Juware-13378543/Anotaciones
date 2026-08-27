with open("archivos/texto.txt","a",encoding="UTF-8") as archivo:

    #Usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"Linea {i + 1} agregado\n")