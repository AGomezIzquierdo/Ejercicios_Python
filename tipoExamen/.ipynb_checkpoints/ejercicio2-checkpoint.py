
#LAMBDA --> lambda valores_de_entrada : lo_que_haces

def leer_ventas_tapas():

    lista_ventas = []

    for i in range(4):

        nombre_tapa = input("Introduce el nombre de la tapa")
        precio_unitario = int(input("Introduce que precio tiene"))
        cantidad_vendida = int(input("Introduce cuanta cantidad se ha vendido"))

        lista_ventas.append((nombre_tapa, precio_unitario, cantidad_vendida))

    return lista_ventas

def calcular_estadisticas_tapas(lista_ventas):

    estadisticas = {}

    for tapa in lista_ventas:
        total = tapa[1] * tapa[2]

        iva_aplicado = total * 0.1

        if(tapa[2] > 25):
            popularidad = "Alta"
        elif(tapa[2] > 15):
            popularidad = "Media"
        else:
            popularidad = "Baja"
        
        estadisticas[tapa[0]] = (total, iva_aplicado, popularidad)

    return estadisticas


def analizar_rendimiento_tapas(dic_estadisticas):
    
    # 1. Filtrar tapas con popularidad Alta
    tapas_alta_popularidad = [
        (nombre, datos[0])
        for nombre, datos in dic_estadisticas.items()
        if datos[2] == "Alta"
    ]

    # 2. Calcular promedio de IVA
    promedio_iva = sum(
        map(lambda datos: datos[1], dic_estadisticas.values())
    ) / len(dic_estadisticas)

    # 3. Encontrar tapa con mayor recaudación
    tapa_top = max(
        dic_estadisticas,
        key=lambda nombre: dic_estadisticas[nombre][0]
    )

    return (tapas_alta_popularidad, promedio_iva, tapa_top)

#MAIN

lista_ventas = leer_ventas_tapas()
print(lista_ventas)

diccionario_estadisticas = calcular_estadisticas_tapas(lista_ventas)
print(diccionario_estadisticas)

resultado = analizar_rendimiento_tapas(diccionario_estadisticas)
print(resultado)














