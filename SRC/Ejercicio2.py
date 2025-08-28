# Determinar si el numero es par o impar 
Numero = int(input("Ingrese un numero entero: "))
residuo = Numero % 2
# Si residuo es 0, el numero es par
if residuo == 0:
    print("El numero es par")
else:
    print("El numero es impar") 
    