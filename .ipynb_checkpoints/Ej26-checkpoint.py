
matriz = []

for i in range(3):
    fila = []

    for j in range(3):
        numero = int(input("Introduzca un número: "))
        fila.append(numero)

    matriz.append(fila) 

print("Matriz introducida:")

for i in range(3):
    print(matriz[i])

cuadrado = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        for k in range(3):
            cuadrado[i][j] = cuadrado[i][j] + matriz[i][k] * matriz[k][j]

print("Matriz al cuadrado:")

for i in range(3):
    print(cuadrado[i])