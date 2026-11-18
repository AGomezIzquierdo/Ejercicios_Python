class Empleado:

    def __init__(self, nombre, salario_base):
        self.__nombre = nombre
        self.__salario_base = salario_base

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base = salario_base

    def calcular_salario(self, irpf):
        salario_neto = self.salario_base - (self.salario_base * irpf / 100)
        return salario_neto
    
    def __str__(self):
        return(f"Nombre:{self.nombre}, "
               f"Salario base: {self.salario_base}, ")

class Vendedor(Empleado):

    def __init__(self, nombre, salario_base, ventas_realizadas):
        super().__init__(nombre, salario_base)
        self.__ventas_realizadas = ventas_realizadas

    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas.copy()

    def calcular_salario(self):
        total_ventas = sum(self.ventas_realizadas)
        salario_total = self.salario_base + (total_ventas * 0.1)
        return salario_total

    def agregar_venta(self, importe):
        self.__ventas_realizadas.append(importe)

    def __str__(self):
        return(f"{super().__str__()}, Ventas: {self.ventas_realizadas}, "
               f"Salario total: {self.calcular_salario()} ")


#MAIN

# Crear dos empleados
empleado1 = Empleado("Alejandro", 100)
empleado2 = Empleado("Marta", 120)

# Crear dos vendedores
vendedor1 = Vendedor("Miguel", 1200, [100, 150, 80])
vendedor2 = Vendedor("Pepe", 1400, [200, 300])

# Mostrar información inicial
print("----- EMPLEADOS -----")
print(empleado1)
print(empleado2)

print("\n----- VENDEDORES -----")
print(vendedor1)
print(vendedor2)

# Modificar atributos usando setters
empleado1.salario_base = 150
vendedor1.salario_base = 1300

# Agregar dos ventas a un vendedor
vendedor1.agregar_venta(200)
vendedor1.agregar_venta(250)

# Mostrar información actualizada
print("\n----- INFORMACIÓN ACTUALIZADA -----")
print(empleado1)
print(vendedor1)

    















    