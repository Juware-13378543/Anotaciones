numeros = [1,2,3,4,5,6,7,8,9]


#Creando una funcion lambda para multiplicar por dos
#Rapida y sencilla, sin usos del return
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(4))


#Creandoun funcion para saber si un numero es par o no
##def es_par(num):
##    if (num%2 == 1):
##        return True
    
#usando filter con una funcion comun
##numeros_pares = filter(es_par, numeros)

#Creando la misma funcion pero con lambda
numero_pares = filter(lambda num : num%2 == 0,numeros)
print(list(numero_pares))


