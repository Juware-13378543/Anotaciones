import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos/dispercion.csv")

#Creando el grafico
sns.scatterplot(x="tiempo",y="dinero",data=df)

#Mostrando el grafico
plt.show()
