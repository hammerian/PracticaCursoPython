#

listado = [2,4,2,6,8,4,2,8,1,6]

posList = input("Introduce una posición del listado:")

valueList = int(listado[int(posList)-1])

txt1 = "El número en la posición: {} Es: {}"

print(txt1.format(int(posList),valueList))

conta = 0

for i in listado:
    if (i == valueList):
        conta+=1
        
txt2 = "El número se repite {} veces."
print(txt2.format(int(conta)))
