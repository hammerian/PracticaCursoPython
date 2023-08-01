# -*- coding: utf-8 -*-
numero1 = input("introduce el primer número para comparar:")
numero2 = input("introduce el segundo número para comparar:")
n1 = int(numero1)
n2 = int(numero2)
if n1 > n2:
  print("La suma de los números es: ",(n1+n2),"\nLa diferencia de los números es: ",(n1-n2))
else:
    print("El producto de los números es: ",(n1*n2),"\nLa división de los números es: ",(n1/n2))