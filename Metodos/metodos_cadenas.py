cadena1 = "Hola, soy, Julian"
cadena2 = "Bienvenido como estan"

#Estructura es El  "dato.Metodo(parametros)"

# Se usa para saber que funciones, se pueden Usar
resultado=dir(cadena1)

#NOMENCLATURA
resultado2=cadena1.upper()#Se usa para Dar mayusculas
resultado3=cadena1.lower()#Se usa para Dar minusculas
resultado4=cadena1.capitalize()#Se usa para poner la primera en mayuscula

#Coincidencias o Rastreo
resultado5=cadena1.find("J")#Busca una cadena, en otra cadena si hay coinsidencias
#Son similares pero hace Exepciones
resultado6=cadena1.index("J")#Busca y alarma , si no hay coincidencia

#SI ES NUMERICO DEVUELVE (TRUE) SI NO (FALSE)
resultado7=cadena1.isnumeric()

#SI ES ALFANUMERICO DEVUELVE TRUE SI NO FALSE
resultado8=cadena1.isalpha()#No cuenta los espacios. solo contiene A-Z

#Cuenta las coincidencias de una cadena,dentro de otra cadena,devuelve la cantidad de coincidencias
#Cuenta todas las coincidencias, que se pregunta.
resultado9=cadena1.count("a")

#Cuenta cuantos caracteres tine una cadena
resultado10=len(cadena1)

#Verifica si una cadena empieza con otra cadena dada, si es asi devuelve True
resultado11=cadena1.startswith("Hola")
resultado12=cadena1.startswith("hola")

#Verifica si una cadena termina con otra cadena dada, si es asi devuelve true
resultado13=cadena1.endswith("n")

#Remplaza un pedazo de cadena, por otra dada
resultado14=cadena2.replace("estan","estais mis compañeros")

#Separar caedenas con la cadena que le pasemos
cadena_separada=cadena1.split(",")

#Rempleza un opedazo de cadena dada por otra solicitada
print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)
print(resultado8)
print(resultado9)
print(resultado10)
print(f"Palabra clave es: \"Hola\" Si le acerta es: {resultado11} ,si no seria {resultado12}")
print(resultado13)
print(resultado14)
print(cadena_separada)