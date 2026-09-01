import pandas as pd

#Usando la funcion read_csv para leer el archivo csv
df = pd.read_csv("leer csv/datos.csv",names=["name","lastname","age"])
df2 = pd.read_csv("leer csv/datos.csv",names=["name","lastname","age"])

#Df significa : data frame similar a hojas de calculos
print(df)

#Obteniendo los datos de la columna nombre
print(df["name"])

#Obteniendo los datos de la columna apellido
print(df["lastname"])

#Obteniendo los datos de la columna edad
print(df["age"])


#Tecnica slysing
cadena = "0123456789"
print(cadena[4:8])

#Ordenar datos por la edad
df_ordenado_ascendente = df.sort_values("age")

#Ordenando de forma decsendente
df_ordenado_descendente = df.sort_values("age",ascending=False)

print(df_ordenado_ascendente)
print(df_ordenado_descendente)

#Concatenando los 2 dataframe
df_concatenando = pd.concat([df,df2])

#Accediendo a la primeras 3 filas con head()
primer_fila = df.head(3)
print(primer_fila)

#Accediendo a las ultimas 3 filas con tail()
ultima_fila = df.tail(3)
print(ultima_fila)

#Accediendo a la cantidad de filas y columnas con shape
filas_totales,columna_totales = df.shape

#Obteniendo data estadistica del data frame
df_info = df.describe()

print(df_info)

#Accediendo a un elemento especifico del df con loc edad fila 2
elemento_especifico_loc = df.loc[2,"age"]

#Accediendo a un elemento especifico del df con iloc edad fila 2
elemento_especifico_iloc = df.iloc[2,2]
print(elemento_especifico_loc)

#Accediendo a todas las filas de una columna
apellido = df.loc[2,:]
print(apellido)