
t = [1, 2, 3, 4, 5]

ordenado = True

for i in range(len(t) - 1):
    if t[i] > t[i + 1]:
        ordenado = False

if ordenado:
    print("El vector está ordenado")
else:
    print("El vector no está ordenado")