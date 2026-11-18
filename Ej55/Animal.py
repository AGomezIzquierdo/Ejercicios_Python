class Animal:

    def __init__(self, idAnimal, especie):
        self.__idAnimal = idAnimal
        self.__especies = especie

    @property
    def idAnimal(self):
        return self.__idAnimal

    @property
    def especie(self):
        return self.__especie

    def __str__(self):
        return f"ID: {idAnimal}, Especie : {especie}"
        
        