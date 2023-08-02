# Teniendo un número X pedido por pantalla, queremos:
# Que el número sea divisible por 2. Si no cumple la condición, comprobar que sea por 3.
# Si no lo es, comprobar que sea por 5.
# Si no cumple ninguna condición, mostrar un mensaje por pantalla indicandolo.

numero1 = input("Introduce un número para comprobar:")

n1 = int(numero1)

if n1 % 2 == 0:
    print("El número es divisible por 2")
    if n1 % 3 == 0:
        print("El número es divisible por 3")
        if n1 % 5 == 0:
            print("El número es divisible por 5")            
    elif n1 % 5 == 0:
            print("El número es divisible por 5")
elif n1 % 3 == 0:
    print("El número es divisible por 3")
    if n1 % 5 == 0:
        print("El número es divisible por 5")
    
elif n1 % 5 == 0:
    print("El número es divisible por 5")
    
else:
    print("El número no es divisible por 2, 3, o 5")