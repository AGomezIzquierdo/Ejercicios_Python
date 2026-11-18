
num = int(input("Introduce un número entre 0 y 999"))

if num < 10:
    print("El número tiene 1 cifra")
elif num < 100:
    print("El número tiene 2 cifras")
elif num < 1000:
    print("El número tiene 3 cifras")