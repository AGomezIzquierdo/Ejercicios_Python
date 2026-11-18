
sueldo = int(input("Introduzca el sueldo:"))
antiguedad = int(input("Introduzca la antiguedad:"))

if sueldo < 1500 and antiguedad >= 10:
    sueldo = sueldo * 1.20
elif sueldo < 1500 and antiguedad < 10:
    sueldo = sueldo * 1.05

print("El sueldo actualizado es: ",sueldo)