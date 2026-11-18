import random

randomNum = random.randrange(10);


for i in range(3):

    print("Introduce un numero:")
    numero = int(input())

    if (numero == randomNum):
        print("Correcto")
        break
    elif numero < randomNum:
        print("Mayor")
    else:
        print("Menor")