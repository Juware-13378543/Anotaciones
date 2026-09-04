#Creando funcion para sumar dos numeros y controlar la excepcion de que se ingrese un 
#caracter no numerico
def sumar_dos():
    #Iniciando un bucle
    while True:
        #Pidiendo al usuario que ingrese dos numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #Intentando convertir los numeros a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        #Si lanza una excepcion, se pedira que ingrese un numero y no una letra
        except:
            print("Te pedi un numero, no una letra")
        #Si todo salio bien termina el bucle
        else:
            break
        finally:
            print("Gracias por usar la calculadora")

    #Mostrando el resultado de la suma
    return resultado
    

print(sumar_dos())