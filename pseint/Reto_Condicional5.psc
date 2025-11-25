Algoritmo Reto_Condicional5
    Definir tipo_Docut, nombre, apellido, genero, direccion Como Caracter
    Definir año_Nacimiento, celular Como Entero
    Definir salario, aumento, salario_Final Como Real
	
    Escribir "Ingrese su tipo de documento (CC, PS, CE, CI): "
    Leer tipo_Docut
    Escribir "Ingrese su nombre: "
    Leer nombre
    Escribir "Ingrese su apellido: "
    Leer apellido 
    Escribir "Ingrese su genero (M, F): "
    Leer genero
    Escribir "Ingrese su año de nacimiento: "
    Leer año_Nacimiento
    Escribir "Ingrese su direccion: "
    Leer direccion
    Escribir "Ingrese su numero telefonico: "
    Leer celular
    Escribir "Ingrese su salario: "
    Leer salario
	
	si salario <= 1200000 Entonces
		si (genero = "F") o (genero = "f") Entonces
			aumento = salario * 0.10
		SiNo
			si (genero = "M") o (genero = "m") Entonces
				aumento = salario * 0.08
			FinSi
		FinSi
	FinSi
	
	si (salario >= 1200000) O (salario < 2000000) Entonces
		aumento = salario * 0.05
	finsi
	
	si salario >= 2000000 Entonces
		si (genero = "F") o (genero = "f") Entonces
			aumento = salario * 0.03
		SiNo
			si (genero = "M") o (genero = "m") Entonces
				aumento = salario * 0.025
			FinSi
		FinSi
	FinSi
	
	salario_Final = aumento + salario
	
	Escribir " Reporte final "
	Escribir " El emplead@ ", nombre, "", apellido
	Escribir " Su salario incial era de ", salario
	Escribir " El aumeento del salario es de ", aumento
	Escribir " El salario con el aumento es de ", salario_Final
	
	
FinAlgoritmo