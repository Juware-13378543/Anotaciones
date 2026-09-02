import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos/miguel_ingresos.csv")

#Creando grafico de barras
sns.barplot(x ="fuente", y="ingresos",data=df)

#Obteniendo el total
total_ingresos = df["ingresos"].sum()

#Mostrando el total
print(f"El total de ingresos es de: ${total_ingresos} USD")

#Mostrando el grafico
plt.show()