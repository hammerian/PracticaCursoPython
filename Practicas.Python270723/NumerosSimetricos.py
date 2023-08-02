# Mostrar números desde 1 a un número solicitado y despues volver a 1

numero1 = input("Introduce un número entre 5 y 20:")

n1 = int(numero1)

if (n1 >=5 and n1 <=20):
    txt = ""
    for x in range(n1):
        txt2 = "{}"
        txt = txt + txt2
        txt = txt.format(x+1)
    n1 = n1-1
    for x in range(n1):
        txt2 = "{}"
        txt = txt + txt2
        txt = txt.format(n1-x)

print(txt)