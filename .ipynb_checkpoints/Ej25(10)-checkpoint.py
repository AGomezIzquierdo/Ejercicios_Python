
m = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

traspuesta = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for i in range(len(m)):
    for j in range(len(m)):
        traspuesta[j][i] = m[i][j]

print(traspuesta)