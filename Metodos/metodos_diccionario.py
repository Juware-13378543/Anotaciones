diccionario = {
    "nombre":"Julian Bejarano",
    "Apellido":"Rojas",
    "Juego Fav":"Rd 2"
}

claves =diccionario.keys()#Devuelve las claves 
solicitud =diccionario.get("Juego Fav")#Busca la llave y continua el Programa

#Clear Limpia todo del Diccionario
#diccionario.clear()

#Elimina un elemento de un diccionario
diccionario.pop("Apellido","Rojas")

#Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(claves)#Devuelve las claves 
print(f"Mi juego favorito es: {solicitud}\n\n")
print(diccionario)

print(diccionario_iterable)
