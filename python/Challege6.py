import random

dad = 0
cont_Laz = 1
acum_Dado = 0
cont_Par = 0
cont_Impar = 0

input("Presione ENTER para lanzar dado")
dad = random.randint(1, 6)
acum_Dado = dad
print(f"Lanzamiento 1 dado igual a {dad}")

if dad % 2 == 0:
    cont_Par += 1
else:
    cont_Impar += 1

respuesta = input("¿Quieres seguir lanzando el dado (si/no)? ").lower()

while respuesta == "si":
    cont_Laz += 1
    input("Presione ENTER para lanzar dado")
    dad = random.randint(1, 6)
    acum_Dado += dad
    print(f"Lanzamiento {cont_Laz} dado igual a {dad}")

    if dad % 2 == 0:
        cont_Par += 1
    else:
        cont_Impar += 1

    respuesta = input("¿Quieres seguir lanzando el dado (si/no)? ").lower()

print("Reporte Final")
print(f"El total de lanzamientos fue {cont_Laz}")
print(f"La suma total de los lanzamientos fue {acum_Dado}")
print(f"El total de pares es {cont_Par}")
print(f"El total de impares es {cont_Impar}")

