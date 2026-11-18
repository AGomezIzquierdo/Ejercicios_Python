
suma = 0

for i in range (1, 1001):
    if(i%3 == 0) & (i%7 == 0):
        suma = suma + i

print(suma)