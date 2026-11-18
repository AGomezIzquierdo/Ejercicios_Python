
lista = []

for i in range(3):
    palabra = input("Introduce cualquier palabra")
    lista.append(palabra)

print("La lista creada es: ",lista)

listaVocales = []
listaConsonantes = []

vocales = ["a", "e", "i", "o", "u"]

for palabra in lista:
    if palabra[0].lower() in vocales:
        if palabra not in listaVocales:
            listaVocales.append(palabra)

    else:
        if palabra not in listaConsonantes:
            listaConsonantes.append(palabra)

tuplaCons = tuple(listaConsonantes)

print("Lista de palabras que empiezan por vocal:", listaVocales)
print("Tupla de palabras que empiezan por consonante:", tuplaCons)

