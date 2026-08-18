#falto el profe y los compañeros van a armar la clase

#funcion para obtener al asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):

    #Creando la lista con los compañeros
    compañeros = []

    #Ejecutando un bucle para solicitar la informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = (input("Ingrese el nombre del compañero: "))
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)

        #Agregando el compañero a la lista de compañeros
        compañeros.append(compañero)

    #Ordenando la lista de compañeros por edad y obteniendo al asistente y al profesor
    compañeros.sort(key=lambda x: x[1])

    #Compañero[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #Para definir al asistente y al profesor, tomamos el primer y ultimo elemento de la lista respectivamente
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]

    #Retornamos la tupla
    return asistente,profesor

#Desempaquetando la tupla retornada por la funcion
asistente,profesor = obtener_compañeros(3)

#Mostrando el resultado
print(f"El profesor es: {profesor} y el asistente es: {asistente}")
