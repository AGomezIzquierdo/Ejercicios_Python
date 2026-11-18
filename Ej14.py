
n = int(input("Dame el valor de n:"))

pi = 2

for i in range(1,n+1):
    pi = pi * (2 * i) / (2 * i + 1) * (2 * i) / (2 * i - 1)

print("El valor aprox de PI es: ", pi)