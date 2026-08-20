#Creando una funcion que muestre la serie fibonacci hasta el numero que pasemos como argumento

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = b,a+b

resultado = fibonacci(20)
print(f"Los números de la serie fibonacci hasta 20 son: {resultado}")

