
#

conta = 0
txtLotery = ""

while conta<5:
    num = input("Introduce un número entre 0 y 9:")
    if (int(num) >=0) | (int(num) <9):
        txtLotery = txtLotery + num
        conta += 1
    else:
        print("El número no está entre 0 y 9 :(\n")

print("El número de Lotería es: ",txtLotery) 