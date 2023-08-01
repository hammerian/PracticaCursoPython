# -*- coding: utf-8 -*-
numero1 = input("Introduce la primera nota del alumno:")
numero2 = input("Introduce la segunda nota del alumno:")
numero3 = input("Introduce la tercera nota del alumno:")
n1 = int(numero1)
n2 = int(numero2)
n3 = int(numero3)
promedio = float((n1+n2+n3)/3)
if promedio > 7:
    print("Promocionado")
else:
    print("No promocionado")