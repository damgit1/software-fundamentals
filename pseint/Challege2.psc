Algoritmo Challenge2
	Definir Dad, Num_Lanz, Sum, Acum Como Entero
	Sun = 0
	Escribir " Enter number of dice rolls "
	Leer Num_Lanz
	Para Acum = 1 Hasta Num_Lanz Con Paso 1 Hacer
		Dad = Aleatorio(1,6)
		Sum = Sum + Dad
		Escribir " The roll of the dice " Acum  " was "  Dad
	FinPara
	Escribir " The number of pitches was " Num_Lanz
	Escribir " The total number of throws was "  Sum
FinAlgoritmo
