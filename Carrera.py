#Developer: Juan Sebastian Erazo
#Function 1: Multiplicación de dos Numeros recibidos por consola
#Version: 1.0

#Librerías
import os
from random import randint, uniform, random
 
#Funciones
def dado():
    lanzamiento = randint(1,6)
    return lanzamiento

def basico():
    
    turnos = 1

    if nJugadores == 2:
        player1 = 1
        player2 = 2
        while turnos <=20:

            dado1 = dado()
            dado2 = dado()
    elif nJugadores == 3:
        player1 = 1
        player2 = 2
        player3 = 3
    elif nJugadores == 4:
        player1 = 1
        player2 = 2
        player3 = 3
        player4 = 4
    
    


    return player1
    
#Main
os.system("cls")

print("--------------------------------------")
print("           Juego de Carreras          ")
print("--------------------------------------")
print("")

i = 0
j = 0
k = 0

while  i != 1 :
    nJugadores = int(input("Digite la cantidad de jugadores (min 2 max 4): "))

    if nJugadores < 2 :
        print("No se admiten menos de 2 jugadores")

    elif nJugadores > 4:
        print("No se admiten más de 4 jugadores")
    else:
        i = 1


while  j != 1 :

    os.system("cls")

    print("Numero de jugadores: ", nJugadores)
    print("--------------------------------------")
    print("           Nivel de tablero           ")
    print("--------------------------------------")
    print("")
    print("1. Nivel básico (Tablero de 20 posiciones)")
    print("2. Nivel intermedio (Tablero de 30 posiciones)")
    print("3. Nivel avanzado (Tablero de 50 posiciones)")
    print("")

    nTablero = int(input("Seleccione el nivel del tablero: "))

    if nTablero == 1:
        j = 1
        k = 1

    elif nTablero == 2:
        j = 1
        k = 2
    elif nTablero == 3:
        j = 1
        k = 3
    else:
        print("Seleccione un nivel valido")
        key = input("Press any key to continue...")

