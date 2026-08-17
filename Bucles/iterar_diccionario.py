diccionario = {
    "nombre":"Julian",
    "edad":"18",
    "JuegoFav":"Rd2"
}

#Recorriendo diccionario para obtener la clave
for key in diccionario:
    print(key)

#Recorriendo diccionario con item() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")
