
fichero = open("datos_ej44.txt", "rt")

todo = fichero.read()

todo = todo.upper().replace(","," ").replace("."," ").replace("\n"," ").replace("?", " ").replace("!"," ")

lista_palabras = todo.split(" ")

palabras = {}

for palabra in lista_palabras:
    if palabra not in palabras.keys():
        palabras[palabra] = 1
    else:
        palabras[palabra] += 1

print(palabras)

fichero2 = open("salida_ej44.txt","wt")

for(clave, valor) in palabras.items():
    salida = clave + "," + str(valor) + "\n"

    fichero2.write(salida)

fichero2.close()