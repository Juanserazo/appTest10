#Developer: Juan Sebastian Erazo
#Function 1: Multiplicación de dos Numeros recibidos por consola
#Version: 1.0

#Librerías
import os

#Funciones
def calc(a,b):
    add = a + b
    return add
    
#Main
os.system("cls")

n1 = int(input("Press number 1: "))
n2 = int(input("Press number 2: "))

calc (n1,n2)
print("The answer is: ", calc(n1,n2))
