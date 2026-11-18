
equipos = []

for i in range(3):
    equipo = input("Introduce un equipo:")
    equipos.append(equipo)

print(equipos)

lista = []
listaPuntos = []

for equipo in equipos:
    puntos = 0
    ganados = int(input(f"Introduce los partidos ganados del equipo {equipo}"))
    perdidos = int(input(f"Introduce los partidos perdidos del equipo {equipo}"))
    empatados = int(input(f"Introduce los partidos empatados del equipo {equipo}"))

    puntos = ganados * 3 + empatados

    listaPuntos.append((equipo, puntos))

    lista.append((equipo, ganados, perdidos, empatados))

print(lista)

listaPuntos.sort(key=lambda x: x[1], reverse=True)

print(listaPuntos)



    
    