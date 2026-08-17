#Creando una lista con list([])
lista = list(["hola","Julian",8,46,5])

cadena="hola"
resultado = len(cadena)
resultado2 = len(lista)#Cuenta cuanoos elementos hay en la lista

#Agregar un elemento a la lista
lista.append("JAJAJAJAJA")

#Agregando un elemento a la lista en un indice especifico 
lista.insert(2,"Toma mama")

#Agrega varios elementos a una lista
lista.extend([2023,False])


#Eliminando un elemento de la lista por su indice
lista.pop(0)

#Remueve un elemto de la lista por su valor o su nombre
lista.remove(8)

#Lista.sort su funcion es ordenar
#lista.sort
#Se le puede dar reversa
#lista.sort(reverse=True)

#Elimina todos los valores de la lista
#lista.clear

#Verifica si un elemento se encuentra en la lista
Hi=lista.index(46)#Y da su pocision

print(resultado)
print(resultado2)
print(lista)
print(Hi)