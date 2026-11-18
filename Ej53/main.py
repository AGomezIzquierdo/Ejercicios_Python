from Pieza import Pieza
from PiezaMetalica import PiezaMetalica
from PiezaPlastico import PiezaPlastico
from Producto import Producto


pieza1 = PiezaMetalica("P001", 500, 15.50, "www.fabricante1.com", "Acero")
pieza2 = PiezaPlastico("P002", 200, 8.75, "www.fabricante2.com", 80)
pieza3 = PiezaMetalica("P003", 700, 20.00, "www.fabricante3.com", "Aluminio")
pieza4 = PiezaPlastico("P002", 300, 10.00, "www.fabricante4.com", 90)


producto = Producto("PROD001", "Producto de demostracion")


print(producto.agregarPieza(pieza1))
print(producto.agregarPieza(pieza2))
print(producto.agregarPieza(pieza3))
print(producto.agregarPieza(pieza4))


print("\nLISTADO DE PIEZAS")
print(producto.listadoPiezas())


print(f"Precio total: {producto.precioProducto():.2f} euros")
print(f"Peso total: {producto.pesoProducto()} gramos")