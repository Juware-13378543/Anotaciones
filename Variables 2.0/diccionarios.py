#creando diccionarios con dict
diccionario = dict(nombre = "julian", apellido = "Bejarano")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio"]):"jajaja"}

#Creando diccionarios con fromkeys( con valor "none")
#La funcion de la corchea es separa los valores que se van a iterar

diccionario = dict.fromkeys(["nombre","apellido","suscriptores"])

#Creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido","suscriptores"],"No se")


print(diccionario)

