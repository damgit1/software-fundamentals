from random import randint
Sum = 0
Num_Laz = int (input (" Enter number of dice rolls "))
for Acum in range ( 1, Num_Laz + 1 ):
    Dad = randint (1, 6)
    Sum = Sum + Dad
    print(f" The roll of the dice " ,Acum, "was",Dad)
print(f" The number of pitches was ", Num_Laz)
print(f" The total number of throws was ", Sum)