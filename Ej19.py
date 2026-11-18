mayores = 0
menores = 0
suma = 0

for i in range(10):
    edad = int(input(f"Introduce la edad de la persona numero {i + 1}: "))

    suma = suma + edad

    if edad >= 18:
        mayores = mayores + 1
    else:
        menores = menores + 1

media = suma / 10

print(f"Hay {mayores} mayores")
print(f"Hay {menores} menores")
print(f"La media de edad es: {media}")