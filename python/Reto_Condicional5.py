tipo_Docut = input("Ingrese su tipo de documento (CC, PS, CE, CI): ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
genero = input("Ingrese su genero (M, F): ")
año_Nacimiento = int(input("Ingrese su año de nacimiento: "))
direccion = input("Ingrese su direccion: ")
celular = int(input("Ingrese su numero telefonico: "))
salario = float(input("Ingrese su salario: "))

if salario <= 1200000:
    if genero == "F" or genero == "f":
        aumento = salario * 0.10
      
    else:
        if genero == "M" or genero == "m":
            aumento = salario * 0.08
          

elif salario >= 1200000 and salario < 2000000:
    aumento = salario * 0.05
   

elif salario >= 2000000:
    if genero == "F" or genero == "f":
        aumento = salario * 0.03
        
    else:
        if genero == "M" or genero == "m":
            aumento = salario * 0.025

salario_Final = salario + aumento

print("Reporte final")
print("El emplead@ ", nombre, "", apellido)
print("Su salario inicial era de ", salario)
print("El aumento del salario es de ", aumento)
print("El salario con el aumento es de ", salario_Final)
