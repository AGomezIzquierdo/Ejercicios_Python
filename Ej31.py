
lista = []

for i in range(5):
    palabra = input("Introduce una palabra: ")
    lista.append(palabra)

opcion = 0

while opcion != 4:

    print("\n1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Terminar")

    print("Lista actual:", lista)

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        palabra = input("Introduce la palabra que quieres contar: ")
        contador = lista.count(palabra)
        print("La palabra aparece", contador, "veces")

    elif opcion == 2:
        palabra = input("Introduce la palabra que quieres modificar: ")
        nuevaPalabra = input("Introduce la nueva palabra: ")

        for i in range(len(lista)):
            if lista[i] == palabra:
                lista[i] = nuevaPalabra

    elif opcion == 3:
        palabra = input("Introduce la palabra que quieres eliminar: ")

        while palabra in lista:
            lista.remove(palabra)

    elif opcion == 4:
        print("Programa terminado")

    else:
        print("Opción incorrecta")