from Animal import Animal

class Herbivoro(Animal):

    def __init__(self, idAnimal, especie, kgDia):
        super().__init__(idAnimal, especie)
        self.__kgDia = kgDia

    @property
    def kgDia(self):
        return self.__kgDia

    def __str__(self):
        return f"{super().__str__()}, Kg al dia: {self.kgDia}"