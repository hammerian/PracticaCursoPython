# -*- coding: utf-8 -*-
numero1 = input("Introduce un número para comprobar:")
n1 = int(numero1)
if (n1 >= 0 and n1 < 10):
    print("El número tiene un dígito")
elif (n1 >= 10 and n1 < 100):
    print("El número tiene dos dígitos") 
elif (n1 >= 100 and n1 < 1000):
    print("El número tiene tres dígitos") 
else:
    print("El número es negativo")