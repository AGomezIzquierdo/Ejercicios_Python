
caracter = input("Introduzca una letra o en caso de querer terminar el programa un espacio: ")

vocales = 0
noVocales = 0

while caracter != " ":

    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u" or caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
        print("VOCAL")
        vocales = vocales + 1
    else:
        print("NO VOCAL")
        noVocales = noVocales + 1

    caracter = input("Introduzca una letra o en caso de querer terminar el programa un espacio: ")

print(f"Total de vocales: {vocales}")
print(f"Total de no vocales: {noVocales}")
