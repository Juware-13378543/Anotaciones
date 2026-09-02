#Listas, una con nombres otra con apellidos
nombres = ["luca","Matias","Camila","pedro","Roberto"]
apellidos = ["Beja","Zing","Dalto","Roberti","Cuacua"]

#Registrar esta informacion en un Txt de forma optima

with open("arcivos_problemas/nombres_y_apellidos.txt","w") as arch:
    arch.writelines("los datos son: \n\n")
    [arch.writelines(f"Nobre: {n}\nApellido: {a}\n----------\n")for n,a in zip(nombres,apellidos)]