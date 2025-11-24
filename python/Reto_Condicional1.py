from random import randint

input(" Press enter to roll the dice ")

Dad1 = randint(1, 6)
Dad2 = randint(1, 6)

print(" Dice one is ", Dad1)
print(" Dice two is ", Dad2)

if Dad1 % 2 == 0:
    print("The die 1 is an pair number")
else:
    print(" The die 1 is an odd number ")

if Dad2 % 2 == 0:
    print(" The die 2 is an pair number ")
else:
    print(" The die 2 is an odd number ")

if Dad1 == Dad2:
    print( "YOU WIN")
else:
    print("GAME OVER")