
from math import sqrt

a = int(input("Coeficiente a:"))
b = int(input("Coeficiente b:"))
c = int(input("Coeficiente c:"))

discriminante = b*b -4*a*c

if discriminante < 0:
    print("No tiene solución real")
else:
    sol1 = (-b + sqrt(discriminante)) / (2*a)
    sol2 = (-b - sqrt(discriminante)) / (2*a)

    if sol1 == sol2:
        print ("La solución es:", sol1)
    else:
        print ("La primera solución es:", sol1)
        print ("La segunda solución es:", sol2)