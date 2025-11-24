import os
from random import randint

Lives = 3
Satatus = True
tiros = 0


def roll_dice():
    Dad1 = randint (1,6) 
    Dad2 = randint (1,6)
    return Dad1, Dad2
   

########
while True:
    key = input ("Prees any key to rool dice")
    tiros+=1
    dice = roll_dice()    
    print(f"Daci one: {dice[0]}")
    print(f"Daci two: {dice[1]}")
    
    if (dice[0] + dice[1]) %2 == 0:
        Lives+=1
    else:
        Lives-=1
    print (f"Your lives are like that:", Lives)

    if dice[0] == 6 and dice[1] == 6:
        print ("¡¡You won the roll!!", tiros, "🥳🎉")
        break
    if Lives == 0:
        print("¡¡You lost the roll!!", tiros, "🙁😔")
        break