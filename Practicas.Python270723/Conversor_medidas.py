# Conversor de medidas:
# introducir una distancia en metros y convertirla en centímetros y pies.


numMetros = input("Introduce la distancia en metros:")

centimetros = float(numMetros)*100

pies = float(numMetros)*3.28084
txt="El valor de {} m es {}cm o {}ft"
print(txt.format(numMetros,centimetros,pies))