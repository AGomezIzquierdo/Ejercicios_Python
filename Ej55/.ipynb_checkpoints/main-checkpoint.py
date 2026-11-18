
from Animal import Animal
from Herbivoro import Herbivoro
from Carnivoro import Carnivoro
from Zoologico import Zoologico

zoo = Zoologico()

h1 = Herbivoro(1, "Elefante", 50)
h2 = Herbivoro(2, "Jirafa", 20)

c1 = Carnivoro(3, "Leon", True)
c2 = Carnivoro(4, "Tigre", False)

print("=== ALTAS DE ANIMALES ===")
print(zoo.altaAnimal(h1))
print(zoo.altaAnimal(h2))
print(zoo.altaAnimal(c1))
print(zoo.altaAnimal(c2))

print("\n=== ANIMAL REPETIDO ===")
print(zoo.altaAnimal(h1))

print("\n=== KILOS DE PASTO AL DIA ===")
print(zoo.numKilosPasto())

print("\n=== CARNIVOROS PELIGROSOS ===")
print(zoo.listadoPeligrosos())

print("=== BAJA DE ANIMALES ===")
print(zoo.bajaAnimal(2))
print(zoo.bajaAnimal(10))
