diccionario = { ("ferry",1) : [ 2500 ,350 ], # [ carga, pasajeros ]
                ("mercante",2) : [ 120000, 6500 ], # [ carga, autonomía ]
                ("mercante",3) : [ 200000, 3200 ], # [ carga, autonomía ]
                ("ferry",4) : [ 3520 , 420] , # [ carga, pasajeros ]
              }

def obtenerPasajeros(d):
    #Filtrado para quedarme con los ferrys
    ferrys = filter(lambda item_barco : item_barco[0][0] == "ferry" , d.items())

    pasajeros = map(lambda item_barco : item_barco[1][1], ferrys)

    return tuple(pasajeros)

def mayorCarga(d):
    mercante = filter(lambda item_barco : item_barco[0][0] == "mercante" , d.items())

    carga = filter(lambda item_barco : item_barco[1][0]
    

#Main
resultado = obtenerPasajeros(diccionario)
print(resultado)