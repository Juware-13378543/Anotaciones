frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola Papus"

#Evitando que se coma una manzana con la sentencia continua
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f"Me boy a comer una {fruta}")


#Evitar que el bucle siga ejecutando (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"Me boy a comer una {fruta}")
    if fruta == 'pera':
            break
else:
    print("Ha terminado")
    
print("Bucle terminado")


#Recurrir una cadena de texto