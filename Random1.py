#randint: Genera numeros enteros aleatorios
#uniform: Genera numeros flotantes aleatorios

import os
from random import randint, uniform, random

def Z():
    a = randint(0,100)
    return a

def R():
    b = uniform(0,100)
    return b 

print("The Z randon number generated is: ", Z())
print("The R randon number generated is: ", R())
