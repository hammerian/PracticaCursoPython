#

numero1 = input("Introduce el número de pares:")

n1 = int(numero1)
conta = int(0)

for x in range(n1):
    altura = input("\nIntroduce la altura del triangulo:")
    alt1 = int(altura)
    base = input("\nIntroduce la base del triangulo:")
    bas1 = int(base)
    area = (alt1 * bas1)/2
    if (area > 12):
        conta += 1
    txt = "\nEl triángulo tiene una altura de: {} y una base de: {}, con un área de: {}"
    print(txt.format(alt1,bas1,area))
finalTxt = "\nEl número total de triángulos con área mayor de 12 es: {}"
print(finalTxt.format(conta))