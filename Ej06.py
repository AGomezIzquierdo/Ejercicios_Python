
a = int(input("Introduce el primer número"))
b = int(input("Introduce el segundo número"))
c = int(input("Introduce el tercer número"))

if a >= b and a >= c:
    mayor = a

elif b >= a and b >= c:
    mayor = b

else:
    mayor = c

if a <= b and a <= c:
    menor = a

elif b <= a and b <= c:
    menor = b

else:
    menor = c

print("El número mayor es", mayor)
print("El número menor es", menor)
