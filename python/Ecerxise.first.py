from random import randint # Importa la funcion randint de la libreria ramdom
dad = randint(1,6) # Escoge un numero aleatoria entre 1 y 6 para la variable dad
if dad % 2 != 0: # si el residuo de el valor de dado es diferente a 0 escribe ("El resultado del dado es impar y el valor del dado es", valor del dado generado)
    print("El resultado del dado es impar y el valor del dado es", dad)
else:  # si el residuo de el valor de dado es igual a 0 escribe ("El resultado del dado es par y el valor del dado es", valor del dado generado)
    print("El resultado del dado es par y el valor del dado es", dad)