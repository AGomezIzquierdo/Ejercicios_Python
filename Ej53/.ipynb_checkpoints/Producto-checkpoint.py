class Producto:

    def __init__(self, idProducto, nombre):
        self.__idProducto = idProducto
        self.__nombre = nombre
        self.__piezas = []

    @property
    def idProducto(self):
        return self.__idProducto

    @property
    def nombre(self):
        return self.__nombre

    @property
    def piezas(self):
        return self.__piezas

    def agregarPieza(self, oPieza):
        for pieza in self.__piezas:
            if pieza.idPieza == oPieza.idPieza:
                return "Pieza repetida"

        self.__piezas.append(oPieza)
        return "Alta OK"

    def precioProducto(self):
        precio = 0

        for pieza in self.__piezas:
            precio += pieza.precio

        return precio

    def pesoProducto(self):
        peso = 0

        for pieza in self.__piezas:
            peso += pieza.peso

        return peso

    def listadoPiezas(self):
        listado = f"Producto: {self.nombre}\n"

        for pieza in self.__piezas:
            listado += str(pieza) + "\n"

        return listado