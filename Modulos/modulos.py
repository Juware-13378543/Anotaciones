#Importando un modulo y asignandole el nombre "m_saludar"
#import modulo_saludar as m_saludar


#desde el modulo, importamos dos funciones y les cambiamos los nombres
from modulo_saludar import saludar as saludo_normal, saludo_raro as saludo_jajaja

#creamos las variables con los saludos
saludo_raro = saludo_jajaja("Miguel")
saludo = saludo_normal("Julian")

#Mostramos los resultados
print(saludo)
print(f"\n{saludo_raro}")

#Para ver las propiedades y metodos de el namspace
#print(dir(m_saludar))


#Enrutamiento de modulos

