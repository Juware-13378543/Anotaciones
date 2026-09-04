#Creacion de la excepcion personalizada
class miExcepcion(Exception):
    def __init__(self,err):
        print(f"Error: {err}")

#Lanzando la excepcion personalizada
raise miExcepcion("Jaja, persona poco culta")

#Manejando la excepcion personalizada
try:
    raise miExcepcion("Jaja, persona poco culta")
except:
    print("Se ha lanzado una excepcion")


    