
mes = int(input("Escribe el número de un mes"))

match(mes):
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Tiene 31 dias")
    case 4 | 6 | 9 | 11:
        print("Tiene 30 dias")
    case _:
        print("Tiene 28 dias")
        
        