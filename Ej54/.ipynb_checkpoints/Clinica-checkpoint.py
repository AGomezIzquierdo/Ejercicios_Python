from Gato import Gato
from Perro import Perro


class Clinica:
    def __init__(self):
        self.__mascotas = []

    @property
    def mascotas(self):
        return self.__mascotas

    def altaMascota(self, mascota):
        for m in self.__mascotas:
            if m.idMascota == mascota.idMascota:
                return "Mascota repetida"

        self.__mascotas.append(mascota)
        return "Alta OK"

    def bajaMascota(self, idMascota):
        for m in self.__mascotas:
            if m.idMascota == idMascota:
                self.__mascotas.remove(m)
                return "Mascota dada de baja"

        return "Mascota no localizada"

    def pesoMaximoGato(self):
        gatos = [m for m in self.__mascotas if isinstance(m, Gato)]

        if len(gatos) == 0:
            return 0

        gatoMayor = max(gatos, key=lambda g: g.peso)
        return int(gatoMayor.peso * 1000)

    def listadoPerros(self):
        texto = ""

        for m in self.__mascotas:
            if isinstance(m, Perro):
                texto += str(m) + "\n"

        if texto == "":
            return "No hay perros registrados"

        return texto.rstrip()