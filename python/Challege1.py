from random import randint
input(" Press enter to roll the dice ")
Dad = randint (1, 6) 
print (f" The number generated on the dice es " ,Dad, " what is ", "pair" if Dad %2 == 0 else "odd")