
t = []

for i in range(5):
    x = int(input("Introduzca un número:"))
    t.append(x)

tuplaT = tuple(t)

print(tuplaT)

lista = []

for numero in tuplaT:
    if numero % 2 == 0:
        lista.append((numero, "PAR"))
    else:
        lista.append((numero, "IMPAR"))

print(lista)