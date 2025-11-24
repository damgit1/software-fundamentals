Algoritmo Challege5
	
	Definir num_lanz, dad, cont, pares, impares Como Entero

	pares = 0
	impares = 0
	Escribir " Ingrese el numero de veces que desee lanzar el dado "
	Leer num_lanz
	Para cont = 1 Hasta num_lanz Con Paso 1 Hacer

		dad = Aleatorio(1,6)
		Escribir "Lanzamiento ", cont, " fue ", dad

		Si dad MOD 2 = 0 Entonces
			pares = pares + 1
		SiNo
			impares = impares + 1
		FinSi
	FinPara
	
	Escribir 'Total de pares: ', pares
	Escribir 'Total de impares: ', impares
FinAlgoritmo
