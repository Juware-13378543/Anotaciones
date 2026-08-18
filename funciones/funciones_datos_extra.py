#Creando una funcion de 3 parametros
#def frase (nombre,apellido,adjetivo):
#    return f"hola {nombre} {apellido} sos muy {adjetivo}"

#Utilizando keywords arguments
#frase_resultante = frase(apellido = "Rojas",adjetivo = "bello",nombre = "Julian")

#Creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo = "Raro"):
    return f"{nombre} {apellido} eres muy {adjetivo}"

frase_final = frase("Julian","Bejarano","inteligente")
print(frase_final)            