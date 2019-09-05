#Developer: Juan Sebastian Erazo - Juan Sebastian Delgado
#Factorial
#Version: 1.0

#Librerias
import os

#Limpiar pantalla
os.system("cls")

print("---------------------------------")
print("            FACTORIAL")
print("---------------------------------")

#Entrada del numero a realizar el factorial

numero = input("Escriba el numero para realizar factorial: ")
apuntador = int(numero)
resultado = 1
z = 1
while z <= apuntador:
    resultado = resultado * z
    z = z + 1
print("El factorial del numero ",numero, "! es ",resultado)