from random import randint

cont = 0
Dad1 = 0
Dad2 = 0

num_Lanz = int(input("Ingresar el número de veces que desea lanzar el dado: "))

while not ((Dad1 == 6 and Dad2 == 6) or (cont == num_Lanz)):
    cont += 1
    input("Presiona ENTER para lanzar los dados")
    Dad1 = randint(1, 6)
    Dad2 = randint(1, 6)
    print(f"El dado 1 en el lanzamiento {cont} fue de {Dad1}")
    print(f"El dado 2 en el lanzamiento {cont} fue de {Dad2}")

if Dad1 == 6 and Dad2 == 6:
    print("¡Ganaste! Haz sacado un par de 6")
else:
    print("Perdiste. En tus lanzamientos no sacaste un par de 6")