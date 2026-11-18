
trabajadores =  ["Pedro", "María", "Pedro", "Juan", "María", "Marta"]

asistencia = {}

for trabajador in trabajadores:
    
    if trabajador not in asistencia:
        asistencia[trabajador] = True
    else:
        asistencia[trabajador] = not asistencia[trabajador]

print(asistencia)

dentro = []

for trabajador in asistencia:
    if asistencia[trabajador] == True:
        dentro.append(trabajador)

print(dentro)
        