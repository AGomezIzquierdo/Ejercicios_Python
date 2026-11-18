
sumaPos = 0
sumaNeg = 0
contPos = 0
contNeg = 0

for i in range(10):

    numero = int(input("Introduce un número entero:"))

    if numero >= 0:
        sumaPos = sumaPos + numero
        contPos = contPos + 1
    else:
        sumaNeg = sumaNeg + numero
        contNeg = contNeg + 1

if contPos == 0:
    print("No se han introducido números positivos")
else:
    print(f"La suma de los números positivos es: {sumaPos}")

if contNeg == 0:
    print("No se han introducido números negativos")
else:
    media = sumaNeg / contNeg
    print(f"La media de los números negativos es: {media}")

    