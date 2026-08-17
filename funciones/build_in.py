numeros = [4,7,1,42,15]

#Encontrando el numero mayor de la lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Encontrando el numero menor de la lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondear a 6 decimales
numero = round(12.349898965, 2)
print(numero)

#retorna False -> 0, vacio, False, ninguno \ True -> distinto a 0, true, cadena, datos no vacio
resultado_bool = bool (True)
print(resultado_bool)

#retorna True, si todo los valore son verdaderos
resultado_all = all([0,"true",[344,23]])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)