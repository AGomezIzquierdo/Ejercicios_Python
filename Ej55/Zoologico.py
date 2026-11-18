from Animal import Animal
from Herbivoro import Herbivoro
from Carnivoro import Carnivoro

class Zoologico:

    def __init__(self):
        self.__animales = []

    @property
    def animales(self):
        return self.__animales

    def altaAnimal(self, animal):
        for a in self.__animales:
            if a.idAnimal == animal.idAnimal:
                return "Animal repetido"

        self.__animales.append(animal)
        return "Animal dado de alta"

    def bajaAnimal(self, idAnimal):
        for a in self.__animales:
            if a.idAnimal == idAnimal:
                self.__animales.remove(a)
                return "Animal dado de baja"

        return "No se ha podido encontrar el animal"

    
    def numKilosPasto(self):
        total = 0

        for a in self.__animales:
            if isinstance(a, Herbivoro):
                total += a.kgDia

        return total

    
    def listadoPeligrosos(self):
        listado = ""

        for a in self.__animales:
            if isinstance(a, Carnivoro) and a.peligroso:
                listado += str(a) + "\n"

        return listado





