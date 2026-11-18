t = [4, 8, 2, 9, 5]

x = int(input("Introduzca el elemento a buscar: "))

exito = False

for i in range(len(t)):
    if t[i] == x:
        p = i
        exito = True
        break

if exito:
    print("Elemento encontrado en la posición:", p)
else:
    print("Elemento no encontrado")