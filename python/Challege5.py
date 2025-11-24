from random import randint
import os

num_lanz = int(input("Ingrese el numero de veces que desee lanzar el dado  "))

pares = 0
impares = 0


for cont in range(1, num_lanz + 1):
    dad = randint(1, 6)
    print("Lanzamiento", cont, "fue", dad)

    if dad % 2 == 0:
        pares += 1
    else:
        impares += 1

os.system('clear')

print("Total de pares:", pares)
print("Total de impares:", impares)