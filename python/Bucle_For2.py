import random
random.seed()   #Prepare random number generator

incr = 1
contPar = 0
contImp = 0
acumTol = 0
print(" How many numbers?; ")
num = int(input())
for incr in range(1, num + 1, 1):
    ramNum = int(random.random() * 100)
    print(ramNum)
    if ramNum % 2 == 0:
        contPar = contPar + 1
    else:
        contImp = contImp + 1
    acumTol = acumTol + ramNum
print(" Total number of pairs generated: " + str(contPar))
print(" Total number of odd generated: " + str(contImp))
print(" The total sum of the generated numbers is: " + str(acumtol))
