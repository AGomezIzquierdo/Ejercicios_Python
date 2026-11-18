
t = [4, 89, 2, 54]

mayor = t[0]
menor = t[0]

for i in range(len(t)):

    if t[i] >= mayor:
        mayor = t[i]
    if t[i] <= menor:
        menor = t[i]

print(f"El mayor es {mayor}.")
print(f"El menor es {menor}.")