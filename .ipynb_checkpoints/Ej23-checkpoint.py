
numero1 = int(input("Introduce un número:"))
numero2 = int(input("Introduce el segundo número:"))

for i in range(numero1, numero2 +1):
    if i % 7 == 0:
        print(i)