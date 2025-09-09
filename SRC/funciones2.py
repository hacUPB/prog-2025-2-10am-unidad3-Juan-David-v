"""
crear una funcion llamada menu()
parametros de entrada: ninguno
lo que realiza: muestra un menu y pide al usuario que seleccione una opcion.
Valor de retorno: la opcion seleccionada
"""

def menu():
    print("1. Entradas\n2. Platos fuertes\n3. Bebidas\n4. Postres\n5. salir")
    opcion = int(input("Elija una opcion: "))
    return opcion

def entradas():
    print("1. pandebono\t\t$3000")
    print("2. Empanada\t\t$3500")

def platos_fuertes():
    print("1. bandeja paisa\t\t$30000")
    print("2. sancocho\t\t$20000")

def bebidas(): 
    print("1. limonada\t\t$7000")
    print("2. jugos naturales\t\t$7000")

def postres():
    print("1. torta\t\t$4000")
    print("2. Arroz con leche\t\t$7000") 


# Funcion principal
eleccion = menu()
print(eleccion)

match(eleccion):
    case 1:
        entradas()
    case 2:
        platos_fuertes()
    case 3:
        bebidas()
    case 4:
        postres()
    case _:
        print("opcion no valida")
