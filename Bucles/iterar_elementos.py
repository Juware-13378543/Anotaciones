animales = ["gato","perro","loro","cocodrilo"]
numeros = [10,20,30,12,74]


#recorriendola lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")

#recorriendo la lista de numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero *10
    print(resultado)


#Se imprimen dos listas en intercalacion
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")


#Cuenta una cantidad limitada por mi
#Forma no optima de recorre una lista
for num in range(1,10):
    print(num)


#Forma optima de recorre una lista con un indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es {valor}")

#Usando el else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle a finalizado")

#Todo lo anterior sirve para iterear listas y tuplas