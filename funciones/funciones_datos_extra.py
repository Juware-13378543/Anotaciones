#Creando una funcion de 3 parametros
def frase (nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido} sos muy {adjetivo}"

#Utilizando keywords arguments
frase_resultante = frase(apellido = "Rojas",adjetivo = "bello",nombre = "Julian")
print(frase_resultante)