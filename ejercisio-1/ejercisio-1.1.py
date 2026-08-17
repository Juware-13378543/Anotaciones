#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso = 1.5

#Duracion de contenido crudo
crudo_promedio = 5
crudo_curso = 3.5

#Diferencia del curso
diferencia_con_min = 100 - (curso / otros_cursos_min * 100)
diferencia_con_max = 100 - (curso * 1000 // otros_cursos_max /10)
diferencia_con_promedio = 100 - (curso / otros_cursos_promedio * 100)

#Calculando el porcentaje de tiempo vacio
tiempo_vacio_promedio = 100 - (otros_cursos_promedio * 1000 // crudo_promedio /10)
tiempo_vacio_curso = 100 - (curso * 1000 // crudo_curso /10)


#Mostrano las diferencias de duracion (ejercisio A)
print("\nEl curso dura: ")
print(f"-El curso visto dura un: {diferencia_con_min}% menos que el mas rapido")
print(f"-El curso visto dura un: {diferencia_con_max}% menos que el mas largo")
print(f"-El curso visto dura un: {diferencia_con_promedio}% menos que el mas comun")

#Mostrando la cantidad de espacios vacios que se remueven (ejercisio B)
print(f"\n-Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"-Este curso elimino el {tiempo_vacio_curso}% de tiempo vacio")

#Mostrando diferencia si los cursos duranran 10 horas
print(f"\n-Ver 10 horas de este curso equvale a ver {otros_cursos_promedio * 100 // curso/10} horas de otros cursos")
print(f"-Ver 10 horas de otroscursos equvale a ver {curso * 100 // otros_cursos_promedio / 10} horas de este curso")





