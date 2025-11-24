from random import randint

Op1 = 0
Op2 = 0
Op3 = 0
Op4 = 0
Op5 = 0
Op6 = 0

Num_Laz = int (input (" Enter number of dice rolls "))
for Acum in range ( 1, Num_Laz + 1 ):
    Dad = randint (1, 6)
    print(f" The roll of the dice " ,Acum, "was",Dad)
    if Dad == 1:
     Op1 = Op1 + 1
    elif Dad == 2:
     Op2 = Op2 + 1
    elif Dad == 3:
     Op3 = Op3 + 1
    elif Dad == 4:
     Op4 = Op4 + 1
    elif Dad == 5:
     Op5 = Op5 + 1
    elif Dad == 6:
     Op6 = Op6 + 1

print(f" The number one came out " ,Op1," times. ")
print(f" The number two came out " ,Op2," times. ")
print(f" The number three came out " ,Op3," times. ")
print(f" The number four came out " ,Op4," times. ")
print(f" The number five came out " ,Op5," times. ")
print(f" The number six came out "  ,Op6," times. ")