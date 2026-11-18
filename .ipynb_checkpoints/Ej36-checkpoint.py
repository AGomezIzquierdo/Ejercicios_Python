
frase = input("Introduce una frase:")

frase.lower()

diccionario = {}

for signo in ".,:;¡!¿?":
    frase = frase.replace(signo, "")

palabras = frase.split()

for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1

print(diccionario)