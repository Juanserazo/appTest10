#CALCULANDO EL FACTORIAL DE UN NÚMERO ("n").
 
#FUNCIÓN PARA CALCULAR EL FACTORIAL.
 
y = input("Type a number:")
x = int(y)
count = 1
z = 1
while z <= x:
    count = count * z
    z = z + 1
print(count)