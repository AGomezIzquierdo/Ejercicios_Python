movimientos = []

for i in range(5):
    concepto = input("Introduce el concepto: ")
    cantidad = float(input("Introduce la cantidad: "))

    movimientos.append((concepto, cantidad))

ingresos = []
gastos = []

for movimiento in movimientos:
    if movimiento[1] > 0:
        ingresos.append(movimiento)
    else:
        gastos.append(movimiento)

totalIngresos = 0
totalGastos = 0

for ingreso in ingresos:
    totalIngresos = totalIngresos + ingreso[1]

for gasto in gastos:
    totalGastos = totalGastos + gasto[1]

print("Lista de ingresos:", ingresos)
print("Lista de gastos:", gastos)
print("Total de ingresos:", totalIngresos)
print("Total de gastos:", totalGastos)