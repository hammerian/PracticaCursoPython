import re

# Introducir una contraseña
valid = False
while valid == False:
    numero2 = input("Introduce una contraseña númerica de 6 cifras:")

    regResult = re.findall("^[0-9]{6}", numero2)

    if regResult:
        print (numero2)
        if numero2 == "123456":
            valid = True
            print ("La contraseña es válida.")
        else:
            print ("La contraseña es incorrecta.")
    else:
        print ("La contraseña no es válida.")

