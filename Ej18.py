
num = int(input("Introduce un número entero:"))

primo = True

for i in range(2, num):
    if num % i == 0:
        primo = False

if primo == False:
    print("No es primo")
else:
    print("Si es primo")