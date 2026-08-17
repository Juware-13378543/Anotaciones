ingreso_mensual = 81000
gasto_mensual = 50000

#Comparadores compuestos
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en Deficit")
    elif ingreso_mensual - gasto_mensual  > 3000:
        print("Estas Bien")
    else:
        print("Estas gastando una banda")        

elif ingreso_mensual > 1000:
    print("Estas bien en latino America")

elif ingreso_mensual > 500:
    print("Estas bien en Argentina")

elif ingreso_mensual > 200:
    print("Estas bien en Venezuela")

else:
    print("Eres pobre")