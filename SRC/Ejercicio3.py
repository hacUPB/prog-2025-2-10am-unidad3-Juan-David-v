#Condicional Simple: 
#Se le pide al usuario que ingrese un numero entero y que muestre un mensaje si el numero es divisible por 3.
 
numero = int(input("Ingresar el numero; "))

residuo=( numero % 3)

if residuo == 0:
    print(numero, "es divisible en 3")