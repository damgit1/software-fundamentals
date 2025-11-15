numberx = 10
print(type(numberx))
numberx = 10.5
print(type(numberx))
numberx = 8j
print(type(numberx))

n1 = "1"
n2 = "4"
add = n1 + n2
print(add)

sumadats = True + True + True
print (f"La suma de datos es :{sumadats}")
print(type(sumadats))

sumadats = True and False
print (f"La suma de datos es :{sumadats}")
print(type(sumadats))

print("##############################")
print("p and q")
print("##############################")
print(f" V ∧ V: {True & True}")
print(f" V ∧ f: {True & False}")
print(f" F ∧ V: {False & True}")
print(f" F ∧ F: {False & False}")

print("##############################")
print("p or q")
print("##############################")
print(f" V ∨ V: {True or True}")
print(f" V ∨ f: {True or False}")
print(f" F ∨ V: {False or True}")
print(f" F ∨ F: {False or False}")

print("Hola" * 3)
print("Hola \n" * 3)
div = 10 / 3
print("Div con /:", div)
print (type(div))

## la doble division da la parte entera
div = 10 // 3
print("Div con //:", div)
print (type(div))

