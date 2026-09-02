#Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas_resuelto/datos.csv")

#Convertir a string los datos de una columna
df["edad"] = df["edad"].astype(str)

#Mostrar el tipo de datos del primer elemento de la columna edad
#print(type(df["edad"][0]))

#Remplazando los datos dalto por maestro
df["apellido"].replace("rojas","maestro",inplace=True)

#Mostrando lacolumna apellido
print(df["apellido"])

#Eliminando las filas repetidas sin datos
df = df.dropna()

#Eliminando las filas repetidas
df = df.drop_duplicates()

#Creando un csv con el dataframe resulatante (limpio)
df.to_csv("archivos_problemas/datos_limpios.csv")