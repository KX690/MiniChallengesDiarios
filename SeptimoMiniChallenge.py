import random

oponente= random.randint(1,3)
opcion=0

def menu():
    print(" Elija una opcion: \n")
    print("1. Piedra \n")
    print("2. Papel \n")
    print("3. Tijera \n")
    print("4. Salir \n")
while (opcion!=4):
    menu()
    opcion=int(input("Elija una opcion"))
    while(opcion<1 or opcion>4):
        menu()
        opcion=int(input("Introduzca una opcion valida: "))

    match oponente:
        case 1: 
            if(opcion == 1):
                print("Es un empate")
            elif(opcion == 2):
                print("El oponente saco piedra, ganaste")
            else:
                print("El oponente saco piedra, perdiste")
        case 2: 
            if(opcion == 1):
                print("El oponenete saco papel, perdiste")
            elif(opcion == 2):
                print("Es un empate")
            else:
                print("El oponente saco papel, ganaste" )
        case 3: 
            if(opcion == 1):
                print("El oponente saco tijera, ganaste")
            elif(opcion == 2):
                print("El oponente saco tijera, perdiste")
            else:
                print("Es un empate")
