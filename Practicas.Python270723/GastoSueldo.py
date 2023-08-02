# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
# realizar un programa que lea los sueldos que cobra cada empleado e informe
# cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
# Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

cantSueldos = input ("Introduce la cantidad de sueldos a contar:")

cantidad = int(cantSueldos)

ricos = 0
pobres = 0
conta = 1
sueldos = 0

while (conta <= cantidad):
    txtP = "\nIntroduce el sueldo del empleado {}:"
    txtF = txtP.format(conta)
    sueldo = input (txtF)
    cantSueldo = float(sueldo)
    sueldos = sueldos + cantSueldo
    conta+=1
    if (cantSueldo>300):
        ricos+=1
    elif(cantSueldo<=300):
        pobres+=1
txtSueldo = "Total sueldos {}, Ricos {}, Pobres {}"
print (txtSueldo.format(sueldos,ricos,pobres))