import re

texto = '''Hola, como estan todos 1
Esta es la segunda linea 2
Esta es la tercera linea 3'''

#Haciendo una busqueda de la palabra linea en el texto
resuelto = re.findall('linea', texto)

#\d -> Busca digitos numericos del 0 - 9 
resultado = re.findall(r"\d",texto)

#\D -> Busca todo lo que no sean digitos numericos del 0 - 9
resultado2 = re.findall(r"\D",texto)

#\w -> Busca todo lo que sean caracteres alfanumericos (letras y numeros) y el guion bajo (_)
resultado3 = re.findall(r"\w",texto)

#\W -> Busca todo lo que no sean caracteres alfanumericos (letras y numeros) y el guion bajo (_)
resultado4 = re.findall(r"\W",texto)


print(resuelto)
print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
