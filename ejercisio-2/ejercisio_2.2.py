#Creando una funcion que nos devuelva los numeros primos
#Entre 0 y el argumento que pasaremos

def numeros_primos(num):
    for i in range(2,num-1):
        if num%i==0:return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3, num+1):
        resultado = numeros_primos(i)
        if resultado == True: primos.append(i)
    return primos


resultado = primos_hasta(17)
print(f"Los números primos hasta 17 son: {resultado}")
