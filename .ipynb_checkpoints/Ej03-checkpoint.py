
maxima = int(input("Cuál es la temperatura máxima que debe hacer?"))

minima = int(input("Cuál es la temperatura mínima que debe hacer?"))

actual = int(input("Qué temperatura hace?"))

if actual > maxima:
    print("‘HACE CALOR. SE VA A ENCENDER EL AIRE ACONDICIONADO")
elif actual < minima:
    print("HACE FRÍO. SE VA A ENCENDER LA CALEFACCIÓN")
else:
    print("LA TEMPERATURA ES LA IDEAL")