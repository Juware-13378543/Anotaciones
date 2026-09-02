import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos/bostezo.csv")

#Creando una grafica
sns.lineplot(x="fecha",y="bostezos",data=df)

#Creando un punto en el momento mas alto
plt.plot("01-06",9,"o")

#Mostrando la grafica
plt.show()


