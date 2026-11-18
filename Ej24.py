
filas = int(input("Introduzca el número de filas: "))

for i in range(filas):
    for j in range(filas):
        print(i + j + 2, end=" ")
    print()