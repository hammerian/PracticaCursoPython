# Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información:
# Cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente.
# Se pide confeccionar un programa que ingrese los dos datos por tecladoe informe el nivel
# del mismo según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
# Nivel máximo:  Porcentaje>=90%  
# Nivel medio:  Porcentaje>=75% y <90%
# Nivel regular: Porcentaje>=50% y <75%
# Fuera de nivel: Porcentaje<50%

numeroTotal = input("Introduce el número de respuestas total:")

n1 = int(numeroTotal)

numeroAciertos = input("\nIntroduce el número de respuestas acertadas:")

n2 = int(numeroAciertos)

porcentaje = (n2 / n1) * 100

if (porcentaje >= 90):
    print("\nEl porcentaje de respuestas acertadas es de:",porcentaje,"% El nivel es máximo.")
elif (porcentaje >= 75):
    print("\nEl porcentaje de respuestas acertadas es de:",porcentaje,"% El nivel es medio.")
elif (porcentaje >= 50):
    print("\nEl porcentaje de respuestas acertadas es de:",porcentaje,"% El nivel es regular.")
else:
	print("\nEl porcentaje de respuestas acertadas es de:",porcentaje,"% Está fuera del nivel.")