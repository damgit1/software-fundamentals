Proceso Reto_Condicional1
	
    Definir Dad1, Dad2 Como Entero
	
	Escribir " Press enter to roll the dice "
	Leer Dad1, Dad2

    Dad1 = Aleatorio(1,6)
    Dad2 = Aleatorio(1,6)

    Escribir " Dice one is ", Dad1
    Escribir " Dice two is ", Dad2
	
    Si Dad1 % 2 = 0 Entonces
        Escribir " The die 1 is an pair number "
    SiNo
        Escribir " The die 1 is an odd number "
    FinSi
	
    Si Dad2 % 2 = 0 Entonces
        Escribir  " The die 2 is an pair number "
    SiNo
        Escribir  " The die 2 is an odd number "
    FinSi
	
    Si Dad1 = Dad2 Entonces
        Escribir "YOU WIN"
    SiNo
        Escribir "GAME OVER"
    FinSi
	
FinProceso