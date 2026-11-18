
a = int(input("Introduzca la primera nota:"))
b = int(input("Introduzca la segunda nota:"))
c = int(input("Introduzca la tercera nota:"))
d = int(input("Introduzca la cuarta nota:"))

media = (a+b+c+d)/4

if media < 60:
    calificacion = "E"
elif media < 70:
    calificacion = "D"
elif media < 80:
    calificacion = "C"
elif media < 90:
    calificacion = "B"
else:
    calificacion = "A"

print(calificacion)