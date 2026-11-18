
lista1 = []
lista2 = []

for i in range(3):
    numero = int(input("Introduzca un número: "))
    lista1.append(numero)

for i in range(3):
    numero = int(input("Introduzca un número: "))
    lista2.append(numero)

lista1.sort()
lista2.sort()

tupla = tuple(lista1 + lista2)

print("Primera lista:", lista1)
print("Segunda lista:", lista2)
print("Tupla:", tupla)