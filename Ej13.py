filas = int(input("Introduce las filas: "))

for i in range(filas):
    for j in range(i * 2 + 1):
        print("*", end="")
    print()

