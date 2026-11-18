print("Introduce un numero")

primero = int(input())

print("Introduce otro numero")

segundo = int(input())

print("1. Sumar los números.\n"
      "2. Restar los números.\n"
      "3. Multiplicar los números.\n"
      "4. Dividir los números.")

opcion = int(input("Elige una opción: "))

match opcion:
    case 1:
        suma = primero + segundo
        print(f"La suma es: {suma}")
    case 2:
        resta = primero - segundo
        print(f"La resta es: {resta}")
    case 3:
        multiplicacion = primero * segundo
        print(f"La multiplicación es: {multiplicacion}")
    case 4:
        division = primero / segundo
        print(f"La división es: {division}")
    case _:
        print("La opción no existe")