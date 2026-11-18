
dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")

horarios = {}

while len(horarios) < 5:
    nombre = input("Introduce el nombre del trabajador")
    if nombre in horarios:
        print("Error, trabajador ya introducido")
    dia = input(f"Introduce el dia que trabaja {nombre}")
    elif dia not in dias:
        print("Error, introduce el dia correctamente")
    elif dia in horarios.values():
        print("Ese dia ya está registrado")
    else:
        horarios[nombre] = dia

print(horarios)
