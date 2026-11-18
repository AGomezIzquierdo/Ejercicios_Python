
anyo = int(input("Escriba un año:"))

if (anyo%4 == 0) | (anyo % 100 == 0 & anyo % 400 == 0):
    print("Es bisiesto")

else:
    print("No es bisiesto")