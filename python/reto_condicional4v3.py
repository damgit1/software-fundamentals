# Declarar variables
# Inicializar variables
num1 = 0
num2 = 0

# Get number one
num1 = float(input(" Enter value to number one: "))

# Get number two
num2 = float(input(" Enter value to number two: "))

# Menu de usuario
print('''
      Match menu:
      (1) - Add
      (2) - Subs
      (3) - Mult
      (4) - Div
      (5) - all 
      ''')
opt = float(input(" Prees any option ( 1 - 5 ) "))

match opt:
 case 1:
  res = num1 + num2
  print(" Addition:" + str(res))
 case 2:
  res = num1 - num2
  print(" Substraction: " + str(res))
 case 3:
    res = num1 * num2
    print(" Multiplication: " + str(res))
 case 4:
    if num2 <= 0:
     print(" Invalid option because you cannot divide by zero ")
    else:
     res = num1 / num2
     print(" Division " + str(res))
 case 5:
    if num2 <= 0:
     print(" Invalid option because you cannot divide by zero ")
    else:
     print(" Addition " + str(num1 + num2))
     print(" Sustraction " + str(num1 - num2))
     print(" Multiplication " + str(num1 * num2))
     print(" Division " + str(num1 / num2))
 case _:
    print(" Invalid option ")
