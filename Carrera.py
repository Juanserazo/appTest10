#Developer: Juan Sebastian Erazo - Dario Alejandro Maya
#Function: Carreras de fichas.
#Version: 1.0

#Librerías
import os
from random import randint, uniform, random
 
#Funciones

#lanzamiento de dado llamado luego
def dado():
    lanzamiento = randint(1,6)
    return lanzamiento
#primer tablero nivel basico
def basico():

    #Ok es unicamente return
    #Variables de puntajes 
    ok1 = 0
    turnos = 1
    puntaje1 = 0
    puntaje2 = 0
    puntaje3 = 0
    puntaje4 = 0

    #Condicion si son dos jugadores
    if nJugadores == 2:
        while 1 == 1:
            
            os.system("cls")
            #TURNO JUGADOR 1
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("         Turno del jugador 1")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado() 
            dado2 = dado()
            puntaje1 = puntaje1 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje1)
            continuar = input("Presione cualquier tecla para continuar")

            #Caso de que el jugador 1 sacó pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 1")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje1 = puntaje1 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje1)
                continuar = input("Presione cualquier tecla para continuar")
                #Si vuelve a sacar pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 1")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje1 = puntaje1 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje1)
                    continuar = input("Presione cualquier tecla para continuar")
                    #Si vuelve a sacar pares acaba el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 1 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #Caso de que el jugador 1 pase el juego llegando a la meta (20)
            if puntaje1 >= 20:
                print("El jugador 1 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
            #TURNO JUGADOR 2
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 2")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje2 = puntaje2 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje2)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador sacó pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 2")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje2 = puntaje2 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje2)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador volvió a sacar pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 2")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje2 = puntaje2 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje2)
                    continuar = input("Presione cualquier tecla para continuar")
                    # tres pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 2 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            turnos = turnos + 1
            #caso de que el jugador 2 ganó el juego con mas de 20 puntos 
            if puntaje2 >= 20:
                print("El jugador 2 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break


    #caso de que hay 3 jugadores
    elif nJugadores == 3:
        while 1 == 1:
            
            os.system("cls")

            #TURNO JUGADOR 1
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("         Turno del jugador 1")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje1 = puntaje1 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje1)
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador sacó pares 
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 1")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje1 = puntaje1 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje1)
                continuar = input("Presione cualquier tecla para continuar")
                #segundo pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 1")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje1 = puntaje1 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje1)
                    continuar = input("Presione cualquier tecla para continuar")
                    #tercer par gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 1 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #Caso de que el jugador 1 pasó los 20 puntos
            if puntaje1 >= 20:
                print("El jugador 1 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
            #TURNO JUGADOR 2
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 2")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje2 = puntaje2 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje2)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador sacó pares 
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 2")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje2 = puntaje2 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje2)
                continuar = input("Presione cualquier tecla para continuar")
                #Caso de que sacó dos pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 2")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje2 = puntaje2 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje2)
                    continuar = input("Presione cualquier tecla para continuar")
                    #Caso de que el jugador sacó 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 2 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #Caso de que el jugador pasó los 20 puntos gana
            if puntaje2 >= 20:
                print("El jugador 2 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

            #TURNO JUGADOR 3
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 3")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje3 = puntaje3 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje3)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador saco pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 3")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje3 = puntaje3 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje3)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador sacó 2 pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 3")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje3 = puntaje3 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje3)
                    continuar = input("Presione cualquier tecla para continuar")
                    #Caso de que el jugador saco 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 3 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            turnos = turnos + 1
            if puntaje3 >= 20:
                print("El jugador 3 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

    #Caso de que hay 4 jugadores 
    elif nJugadores == 4:
        while 1 == 1:
            
            os.system("cls")

            #TURNO JUGADOR 1
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("         Turno del jugador 1")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje1 = puntaje1 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje1)
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador sacó pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 1")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje1 = puntaje1 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje1)
                continuar = input("Presione cualquier tecla para continuar")
                #Caso de que el jugador sacó 2 pares repite lanzamiento 
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 1")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje1 = puntaje1 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje1)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que el jugador saco 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 1 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #caso de que el jugador 1 pasó los 20 puntos gana el juego
            if puntaje1 >= 20:
                print("El jugador 1 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
            #TURNO JUGADOR 2
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 2")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje2 = puntaje2 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje2)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador saca pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 2")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje2 = puntaje2 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje2)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador saca pares nuevamente
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 2")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje2 = puntaje2 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje2)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que el jugador saca 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 2 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #caso de que el jugador 2 pasa los 20 puntos gana el juego
            if puntaje2 >= 20:
                print("El jugador 2 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

            #TURNO JUGADOR 3
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 3")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje3 = puntaje3 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje3)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador saca pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 3")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje3 = puntaje3 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje3)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador saca 2 par de pares
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 3")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje3 = puntaje3 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje3)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que el jugador saca 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 3 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #caso de que el jugador pasa los 20 puntos gana el juego
            if puntaje3 >= 20:
                print("El jugador 3 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

            #TURNO JUGADOR 4
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 4")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje4 = puntaje4 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje4)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador saca par
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 4")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje4 = puntaje4 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje4)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador saca 2 pares 
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 4")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje4 = puntaje4 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje4)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que saca 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 4 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            turnos = turnos + 1
            #caso de que el jugador pasa los 20 puntos gana el juego
            if puntaje4 >= 20:
                print("El jugador 4 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
    return ok1

def intermedio():

    #Ok es unicamente return
    #Variables de puntajes 
    ok2 = 0
    turnos = 1
    puntaje1 = 0
    puntaje2 = 0
    puntaje3 = 0
    puntaje4 = 0

    #Condicion si son dos jugadores
    if nJugadores == 2:
        while 1 == 1:
            
            os.system("cls")
            #TURNO JUGADOR 1
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("         Turno del jugador 1")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado() 
            dado2 = dado()
            puntaje1 = puntaje1 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje1)
            continuar = input("Presione cualquier tecla para continuar")

            #Caso de que el jugador 1 sacó pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 1")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje1 = puntaje1 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje1)
                continuar = input("Presione cualquier tecla para continuar")
                #Si vuelve a sacar pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 1")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje1 = puntaje1 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje1)
                    continuar = input("Presione cualquier tecla para continuar")
                    #Si vuelve a sacar pares acaba el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 1 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #Caso de que el jugador 1 pase el juego llegando a la meta (30)
            if puntaje1 >= 30:
                print("El jugador 1 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
            #TURNO JUGADOR 2
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 2")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje2 = puntaje2 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje2)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador sacó pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 2")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje2 = puntaje2 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje2)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador volvió a sacar pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 2")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje2 = puntaje2 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje2)
                    continuar = input("Presione cualquier tecla para continuar")
                    # tres pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 2 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            turnos = turnos + 1
            #caso de que el jugador 2 ganó el juego con mas de 30 puntos 
            if puntaje2 >= 30:
                print("El jugador 2 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break


    #caso de que hay 3 jugadores
    elif nJugadores == 3:
        while 1 == 1:
            
            os.system("cls")

            #TURNO JUGADOR 1
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("         Turno del jugador 1")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje1 = puntaje1 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje1)
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador sacó pares 
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 1")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje1 = puntaje1 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje1)
                continuar = input("Presione cualquier tecla para continuar")
                #segundo pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 1")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje1 = puntaje1 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje1)
                    continuar = input("Presione cualquier tecla para continuar")
                    #tercer par gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 1 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #Caso de que el jugador 1 pasó los 30 puntos
            if puntaje1 >= 30:
                print("El jugador 1 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
            #TURNO JUGADOR 2
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 2")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje2 = puntaje2 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje2)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador sacó pares 
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 2")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje2 = puntaje2 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje2)
                continuar = input("Presione cualquier tecla para continuar")
                #Caso de que sacó dos pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 2")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje2 = puntaje2 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje2)
                    continuar = input("Presione cualquier tecla para continuar")
                    #Caso de que el jugador sacó 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 2 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #Caso de que el jugador pasó los 30 puntos gana
            if puntaje2 >= 30:
                print("El jugador 2 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

            #TURNO JUGADOR 3
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 3")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje3 = puntaje3 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje3)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador saco pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 3")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje3 = puntaje3 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje3)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador sacó 2 pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 3")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje3 = puntaje3 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje3)
                    continuar = input("Presione cualquier tecla para continuar")
                    #Caso de que el jugador saco 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 3 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            turnos = turnos + 1
            if puntaje3 >= 30:
                print("El jugador 3 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

    #Caso de que hay 4 jugadores 
    elif nJugadores == 4:
        while 1 == 1:
            
            os.system("cls")

            #TURNO JUGADOR 1
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("         Turno del jugador 1")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje1 = puntaje1 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje1)
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador sacó pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 1")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje1 = puntaje1 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje1)
                continuar = input("Presione cualquier tecla para continuar")
                #Caso de que el jugador sacó 2 pares repite lanzamiento 
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 1")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje1 = puntaje1 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje1)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que el jugador saco 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 1 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #caso de que el jugador 1 pasó los 30 puntos gana el juego
            if puntaje1 >= 30:
                print("El jugador 1 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
            #TURNO JUGADOR 2
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 2")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje2 = puntaje2 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje2)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador saca pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 2")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje2 = puntaje2 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje2)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador saca pares nuevamente
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 2")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje2 = puntaje2 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje2)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que el jugador saca 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 2 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #caso de que el jugador 2 pasa los 30 puntos gana el juego
            if puntaje2 >= 30:
                print("El jugador 2 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

            #TURNO JUGADOR 3
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 3")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje3 = puntaje3 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje3)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador saca pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 3")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje3 = puntaje3 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje3)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador saca 2 par de pares
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 3")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje3 = puntaje3 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje3)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que el jugador saca 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 3 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #caso de que el jugador pasa los 30 puntos gana el juego
            if puntaje3 >= 30:
                print("El jugador 3 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

            #TURNO JUGADOR 4
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 4")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje4 = puntaje4 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje4)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador saca par
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 4")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje4 = puntaje4 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje4)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador saca 2 pares 
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 4")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje4 = puntaje4 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje4)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que saca 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 4 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            turnos = turnos + 1
            #caso de que el jugador pasa los 30 puntos gana el juego
            if puntaje4 >= 30:
                print("El jugador 4 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
    return ok2

def avanzado():

    #Ok es unicamente return
    #Variables de puntajes 
    ok3 = 0
    turnos = 1
    puntaje1 = 0
    puntaje2 = 0
    puntaje3 = 0
    puntaje4 = 0

    #Condicion si son dos jugadores
    if nJugadores == 2:
        while 1 == 1:
            
            os.system("cls")
            #TURNO JUGADOR 1
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("         Turno del jugador 1")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado() 
            dado2 = dado()
            puntaje1 = puntaje1 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje1)
            continuar = input("Presione cualquier tecla para continuar")

            #Caso de que el jugador 1 sacó pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 1")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje1 = puntaje1 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje1)
                continuar = input("Presione cualquier tecla para continuar")
                #Si vuelve a sacar pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 1")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje1 = puntaje1 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje1)
                    continuar = input("Presione cualquier tecla para continuar")
                    #Si vuelve a sacar pares acaba el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 1 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #Caso de que el jugador 1 pase el juego llegando a la meta (50)
            if puntaje1 >= 50:
                print("El jugador 1 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
            #TURNO JUGADOR 2
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 2")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje2 = puntaje2 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje2)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador sacó pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 2")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje2 = puntaje2 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje2)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador volvió a sacar pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 2")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje2 = puntaje2 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje2)
                    continuar = input("Presione cualquier tecla para continuar")
                    # tres pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 2 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            turnos = turnos + 1
            #caso de que el jugador 2 ganó el juego con mas de 50 puntos 
            if puntaje2 >= 50:
                print("El jugador 2 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break


    #caso de que hay 3 jugadores
    elif nJugadores == 3:
        while 1 == 1:
            
            os.system("cls")

            #TURNO JUGADOR 1
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("         Turno del jugador 1")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje1 = puntaje1 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje1)
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador sacó pares 
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 1")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje1 = puntaje1 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje1)
                continuar = input("Presione cualquier tecla para continuar")
                #segundo pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 1")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje1 = puntaje1 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje1)
                    continuar = input("Presione cualquier tecla para continuar")
                    #tercer par gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 1 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #Caso de que el jugador 1 pasó los 50 puntos
            if puntaje1 >= 50:
                print("El jugador 1 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
            #TURNO JUGADOR 2
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 2")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje2 = puntaje2 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje2)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador sacó pares 
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 2")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje2 = puntaje2 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje2)
                continuar = input("Presione cualquier tecla para continuar")
                #Caso de que sacó dos pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 2")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje2 = puntaje2 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje2)
                    continuar = input("Presione cualquier tecla para continuar")
                    #Caso de que el jugador sacó 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 2 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #Caso de que el jugador pasó los 50 puntos gana
            if puntaje2 >= 50:
                print("El jugador 2 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

            #TURNO JUGADOR 3
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 3")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje3 = puntaje3 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje3)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador saco pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 3")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje3 = puntaje3 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje3)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador sacó 2 pares repite lanzamiento
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 3")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje3 = puntaje3 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje3)
                    continuar = input("Presione cualquier tecla para continuar")
                    #Caso de que el jugador saco 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 3 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            turnos = turnos + 1
            if puntaje3 >= 50:
                print("El jugador 3 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

    #Caso de que hay 4 jugadores 
    elif nJugadores == 4:
        while 1 == 1:
            
            os.system("cls")

            #TURNO JUGADOR 1
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("         Turno del jugador 1")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje1 = puntaje1 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje1)
            continuar = input("Presione cualquier tecla para continuar")
            #Caso de que el jugador sacó pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 1")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje1 = puntaje1 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje1)
                continuar = input("Presione cualquier tecla para continuar")
                #Caso de que el jugador sacó 2 pares repite lanzamiento 
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 1")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje1 = puntaje1 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje1)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que el jugador saco 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 1 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #caso de que el jugador 1 pasó los 50 puntos gana el juego
            if puntaje1 >= 50:
                print("El jugador 1 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
            #TURNO JUGADOR 2
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 2")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje2 = puntaje2 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje2)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador saca pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 2")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje2 = puntaje2 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje2)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador saca pares nuevamente
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 2")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje2 = puntaje2 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje2)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que el jugador saca 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 2 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #caso de que el jugador 2 pasa los 50 puntos gana el juego
            if puntaje2 >= 50:
                print("El jugador 2 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

            #TURNO JUGADOR 3
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 3")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje3 = puntaje3 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje3)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador saca pares
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 3")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje3 = puntaje3 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje3)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador saca 2 par de pares
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 3")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje3 = puntaje3 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje3)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que el jugador saca 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 3 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            #caso de que el jugador pasa los 50 puntos gana el juego
            if puntaje3 >= 50:
                print("El jugador 3 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break

            #TURNO JUGADOR 4
            #-------------------------------------------------------------
            print("")
            print("--------------------------------------")
            print("        Turno del jugador 4")
            print("--------------------------------------")
            print("Lanzamiento numero", turnos)
            dado1 = dado()
            dado2 = dado()
            puntaje4 = puntaje4 + dado1 + dado2
            print("Saco los dados: ", dado1 ," y ", dado2)
            print("Puntaje: ", puntaje4)
            print("")
            continuar = input("Presione cualquier tecla para continuar")
            #caso de que el jugador saca par
            if dado1 == dado2:
                print("Saco 1° par de pares, presione una tecla para lanzar nuevamente...")
                print("")
                print("--------------------------------------")
                print("         Turno del jugador 4")
                print("--------------------------------------")
                print("Lanzamiento numero", turnos)
                dado1 = dado()
                dado2 = dado()
                puntaje4 = puntaje4 + dado1 + dado2
                print("Saco los dados: ", dado1 ," y ", dado2)
                print("Puntaje: ", puntaje4)
                continuar = input("Presione cualquier tecla para continuar")
                #caso de que el jugador saca 2 pares 
                if dado1 == dado2:
                    print("Saco 2° par de pares, presione una tecla para lanzar nuevamente...")
                    print("")
                    print("--------------------------------------")
                    print("         Turno del jugador 4")
                    print("--------------------------------------")
                    print("Lanzamiento numero", turnos)
                    dado1 = dado()
                    dado2 = dado()
                    puntaje4 = puntaje4 + dado1 + dado2
                    print("Saco los dados: ", dado1 ," y ", dado2)
                    print("Puntaje: ", puntaje4)
                    continuar = input("Presione cualquier tecla para continuar")
                    #caso de que saca 3 pares gana el juego
                    if dado1 == dado2:
                        print("Saco 3° par de pares, Ganó el juego el jugador 4 !!! ")
                        continuar = input("Presione enter para salir del juego")
                        break
            turnos = turnos + 1
            #caso de que el jugador pasa los 50 puntos gana el juego
            if puntaje4 >= 50:
                print("El jugador 4 ganó el juego")
                continuar = input("Presione enter para salir del juego")
                break
    return ok3


    
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

    if nTablero == 1:
        basico()
    elif nTablero == 2:
        intermedio()
    elif nTablero == 3:
        avanzado()