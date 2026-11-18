class Mascota:
    def __init__(self, idMascota, peso):
        self.__idMascota = idMascota
        self.__peso = peso

    @property
    def idMascota(self):
        return self.__idMascota

    @property
    def peso(self):
        return self.__peso

    def __str__(self):
        return f"ID: {self.idMascota}, Peso: {self.peso} kilos"