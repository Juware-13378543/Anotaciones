
#Creando una lista (Se puede modificar)
lista = ["Lucas Dalto","Soy Dalto",True,1.70]
#Creando una tupla (No se puede modificar )
tupla = ("Lucas Dalto","Soy Dalto",True,1.70)

#Esto es valido
lista[0] = "Hola"

#Esto no es valido
#tupla[0] = "Hola"

#Creando un conujunto (SET) (no se puede llmar a los elementos por su indice, no almacena los datos)
conjunto = {"Lucas Dalto","Soy Dalto",True,1.70}
#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict)
diccionario = {
    0:"Lucas Dalto",
    'canal':"Bitacora",
    'Estoy emocionado':True,
    'dato_duplicado': "Bitacora"
}

print(diccionario["Estoy emocionado"])

