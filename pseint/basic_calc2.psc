//Algoritm description:
//Basic calc v2
//Get two numbers
//Add, subs, mult, div
//Print results
Algoritmo basic_calc2
	//Define vars and/or const
	Definir n1, n2 Como Entero
	Definir add,subs,mult Como Entero
	Definir div Como Real
	//Inpunts
	Escribir " Enter number 1 and number 2:" // sohw message to user
	Leer n1, n2 //user enter a number 1 an number 2 and program reads it
	//Processes
	add = n1 + n2;
	subs = n1 - n2;
	mult = n1 * n2;
	div = n1 / n2;
	//Outputs
	Mostrar "Addition: ", add;
	Mostrar "Subtraction: ", subs;
	Mostrar "Multiplication: ", mult;
	Mostrar "Division: ", div;
FinAlgoritmo