from Animal import Animal

class Carnivoro(Animal):

    def __init__(self, idAnimal, especie, peligroso):
        super().__init__(idAnimal, especie)
        self.__peligroso = peligroso

    @property
    def peligroso(self):
        return self.__peligroso

    def __str__(self):
        return f"{super().__str__()}, Peligroso: {self.peligroso}"