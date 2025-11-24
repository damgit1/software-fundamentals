Algoritmo Challege4
    Definir Dad1, Dad2, cont, num_Lanz Como Entero
	
    cont = 0
	Dad1 = 0
	Dad2 = 0
	
	Escribir " ingresar el numero de veces que desea lanzar el dado "
	Leer  num_Lanz
	
	Mientras NO (( Dad1 = 6 y Dad2 = 6) o (cont = num_Lanz)) Hacer
		cont = cont + 1
		Escribir " Preione enter para lanzar los dados "
		Leer enter
		Dad1 = Aleatorio(1,6)
        Dad2 = Aleatorio(1,6)
		Escribir " el dado 1 en el lanzamiento" cont " fue de " Dad1
		Escribir " el dado 2 en el lanzamiento" cont " fue de " Dad2
	FinMientras
	
	si Dad1 = 6 y Dad2 = 6 Entonces
		Escribir " Ganaste haz sacado un par de 6 "
	sino 
		Escribir " Perdiste en tus lanzamiento no sacaste un par de 6 "
		
	FinSi
	
FinAlgoritmo
