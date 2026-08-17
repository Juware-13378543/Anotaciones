#Forma no optima de sumar valores
#def suma(lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados +numero
#    return numeros_sumados
#resultado = suma([8,3,9])
#print(resultado)

#Utilizando el operador * como argumento (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es de: {sum(numeros)}"

resultado = suma("Julian",4,5,7,6)
print(resultado)


#Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([4,5,7,6])
print(suma_total)

#Lo mismo que arriba pero utilizando el operador * como parametro (*args)
def suma2 (nombre,*numeros):
    return f"{nombre}, la suma es de: {sum(numeros)}"

resultado3 = suma2("miguel",7,8,9,2,5,6,4,8)
print(resultado3)