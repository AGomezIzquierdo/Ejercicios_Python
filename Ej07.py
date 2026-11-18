
nota = int(input("Introduzca la nota del alumno: "))

if nota < 5:
    calificacion = "Suspenso"
elif nota < 7:
    calificacion = "Aprobado"
elif nota < 9:
    calificacion = "Notable"
elif nota < 10:
    calificacion = "Sobresaliente"
else:
    calificacion = "Matrícula de honor"

print(calificacion)
