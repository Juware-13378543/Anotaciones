#Creando una funcion simple
def saludar():
    print("Hola lucas, mi maestro como estas")

#Ejecuta una funcion simple
saludar()

#Creando una funcion que tenga un parametro
def saludo(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "principe"
    else:
        adjetivo = "amor"

    print(f"Hola {nombre}, mi {adjetivo} ¿como estas?")

saludo("Isa","mujer")
saludo("Julian","hombre")

#Crear una funcion que retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5

    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    print(contraseña)

password = crear_contraseña_random(4)
frase = f"Tu nueva contraseña es_ {password}"
print(frase)
