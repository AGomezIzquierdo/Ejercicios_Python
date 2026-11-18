
m = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

k = int(input("Introduzca la fila: "))

suma = 0

for j in range(len(m)):
    suma = suma + m[k][j]

print("La suma es:", suma)