
nombre = (input("Introduzca el nombre del fichero:"))

#Abrir fichero
fichero = open(nombre, "rt")

#Devuelve lista de lineas al leerlo
lineas = fichero.readlines()

#Cerrar fichero porque ya ha leido lo que tiene
fichero.close()

listaNum = []

for linea in lineas:
    numeros = linea.replace("\n", "").split(";")

    numeros_reales = map(lambda num_string : float(num_string), numeros) #Lo último(numeros) es la lista que le paso y va recorriendola aplicando la funcion lambda en este caso parseando cada num_string

    listaNum.extend(numeros_reales)
    
print("Máximo: ", max(listaNum))
print("Mínimo: ", min(listaNum))
print("Suma: ", sum(listaNum))
print("Media: ", sum(listaNum)/len(listaNum))
        