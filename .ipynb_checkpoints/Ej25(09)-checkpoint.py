
t = [[1,3,4],[2,5,9],[7,8,6]]

x = int(input("Introduzca el elemento a buscar: "))

p = 0
q = 0
exito = false

for i in range(len(t)):
    for j in range(len(t)):
        if t[i][j] == x:
            p = i
            q = j
            exito = true
            
if exito:
    print("Elemento encontrado en:", p, q)
else:
    print("Elemento no encontrado")
    