#Algoritm description:
'''
   Basic calc v1
   Get two numbers
   Add, subs, mult, div
   Print results
'''

import os

os.system('clear')
#1. Initialize vars and/or constants (Inputs)

# Escribir " Enter number 1:" // sohw message to user
#print("Please, enter number 1: ")

#Leer n1 //user enter a number 1 program reads it
num1 = float (input("Please, enter number 1: "))
print(type(num1))

# Escribir " Enter number 2:" // sohw message to user
#print("Please, enter number 2: ")

#Leer n2 //user enter a number 21 program reads it
num2 = float(input("Please, enter number 2: "))
print(type(num2))

#2. Processes
add = num1 + num2
subs = num1 - num2
mult = num1 * num2
div = num1 / num2

#3. Outputs without f-string
print("Addition: ", add, type (add)) 
print("Subtraction: ", subs, type (subs))
print("Multiplication: ", mult, type (mult))
print("Division: ", div, type (div))

# Output with f-string
print("/n")
print(f"Addition: {add}") 
print(f"Subtraction: {subs}")
print(f"Multiplication: {mult}")
print(f"Division: {div}")