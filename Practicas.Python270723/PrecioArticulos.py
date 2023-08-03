#

listaNombres = "a,"
listaNumeros = "0,"
myLoop = True

while (myLoop):
    art1 = input("Introduce un nombre de artículo:")
    listaNombres = listaNombres.join(art1) + ","
    pre1 = input("Introduce un precio para el artículo:")
    listaNumeros = listaNumeros + pre1 + ","
    next = str(input("¿Seguir introduciendo objetos (S/N)?"))
    if ((next == "N") | (next == "n")):
        myLoop = False
    elif ((next == "S") | (next == "s")):
        myLoop = True
    else:
        print("La respuesta es (S/N), lo tomo como un Sí.")
listaNombres = listaNombres[0:(len(listaNombres)-1)]
listaNumeros = listaNumeros[0:(len(listaNumeros)-1)]
arrNombres = listaNombres.split()
arrNumeros = listaNumeros.split()
sumaTotal = int(0)
grande = int(0)
for obj1 in arrNumeros:
    if int(obj1)>grande:
        grande = obj1
    sumaTotal = sumaTotal + obj1
txt2 = "El total es {}\nEl artículo más caro es {}"
print(txt2.format(sumaTotal,grande))
    