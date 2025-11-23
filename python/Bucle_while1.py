import os 
status = True
Sum = 0
cont = 0
cont_par = 0
cont_impar = 0
cont_pos = 0
cont_neg = 0
cont_pos_par = 0
cont_neg_imp = 0
cont_pos_imp = 0
cont_neg_par = 0

while status: 
    Num = int (input("Ingresar numnero (Digitar 0 para terminar el ssitema"))
    Sum+=Num
    if Num != 0:
        cont = cont + 1
        if Num %2 == 0:
            cont_par = cont_par + 1
        else: 
            cont_impar = cont_impar +1

        if Num > 0:
             cont_pos = cont_pos + 1
        else:
            cont_neg = cont_neg + 1

        if Num %2 == 0 and Num > 0:
            cont_pos_par = cont_pos_par + 1
        elif Num %2 == 0 and Num < 0:
            cont_neg_par = cont_neg_par + 1
        elif Num %2 != 0 and Num < 0:
            cont_neg_imp = cont_neg_imp + 1
        else:
            cont_pos_imp = cont_pos_imp + 1
        

    if Num == 0:
        status = False
print(f"La suma total es", Sum)
print(f"El total de numero ingreados fue ", cont)
print(f"La cantidad de numero pares fue ", cont_par)
print(f"La cantidad de numeros impares fue", cont_impar)
print(f"La cantiddad de numeros positvos ingresada fue", cont_pos)
print(f"La cantidad de numeros negativos ingresados fue", cont_neg)
print(f"La cantidad de numeros pares positivos fue", cont_pos_par)
print(f"La cantidad de numeros negativos pares fue ", cont_neg_par)
print(f"La cantidad de numeros impares negativos fue", cont_neg_imp)
print(f"La cantidad de numeros impares positivos fue", cont_pos_imp)