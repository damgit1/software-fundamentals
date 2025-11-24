Algoritmo Challenge6
    Definir dad, cont_Laz, acum_Dado, cont_Par, cont_Impar Como Entero
    Definir respuesta Como Caracter
	
    cont_Laz = 1
    acum_Dado = 0
    cont_Par = 0
    cont_Impar = 0
	
    Escribir "Presione ENTER para lanzar dado"
    Leer enter
    dad = Aleatorio(1,6)
    acum_Dado = dad  
	
    Escribir "Lanzamiento 1 dado igual a ", dad
	
    
    Si dad MOD 2 = 0 Entonces
        cont_Par = cont_Par + 1
    SiNo
        cont_Impar = cont_Impar + 1
    FinSi
	
    Escribir "¿Quieres seguir lanzando el dado (si/no)?"
    Leer respuesta
	
    Mientras Minusculas(respuesta) = "si" Hacer
        cont_Laz = cont_Laz + 1
        Escribir "Presione ENTER para lanzar dado"
        Leer enter
        dad = Aleatorio(1,6)
        acum_Dado = acum_Dado + dad
		
        Escribir "Lanzamiento ", cont_Laz, " dado igual a ", dad
		
        Si dad MOD 2 = 0 Entonces
            cont_Par = cont_Par + 1
        SiNo
            cont_Impar = cont_Impar + 1
        FinSi
		
        Escribir "¿Quieres seguir lanzando el dado (si/no)?"
        Leer respuesta
    FinMientras
	
    Escribir "Reporte Final"
    Escribir "El total de lanzamientos fue ", cont_Laz
    Escribir "La suma total de los lanzamientos fue ", acum_Dado
    Escribir "El total de pares es ", cont_Par
    Escribir "El total de impares es ", cont_Impar
FinAlgoritmo
