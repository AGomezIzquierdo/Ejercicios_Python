from Clinica import Clinica
from Gato import Gato
from Perro import Perro


clinica = Clinica()

gato1 = Gato(1, 4.5, "Siamés")
gato2 = Gato(2, 6, "Persa")
perro1 = Perro(3, 12, 45)
perro2 = Perro(4, 20, 60)

print("ALTAS DE MASCOTAS")
print(clinica.altaMascota(gato1))
print(clinica.altaMascota(gato2))
print(clinica.altaMascota(perro1))
print(clinica.altaMascota(perro2))

print("\nALTA REPETIDA")
print(clinica.altaMascota(gato1))

print("\nLISTADO DE PERROS")
print(clinica.listadoPerros())

print("\nPESO MÁXIMO DE LOS GATOS")
print(clinica.pesoMaximoGato(), "gramos")

print("\nBAJA DE MASCOTAS")
print(clinica.bajaMascota(3))
print(clinica.bajaMascota(10))

print("\nLISTADO DE PERROS ACTUALIZADO")
print(clinica.listadoPerros())