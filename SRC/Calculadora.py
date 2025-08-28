#Calculadora#
control = True
while control == True:
    numero1 = int(input("ingrese el primer numero: "))
    numero2=int(input("ingrese el segundo numero: "))
    print("S. Sumar\nR. Restar \nM. Multiplicar\nD. Dividir\nE. Salir")
    opcion = input("Elija una opcion")


    match opcion:
        case "S":
            print("Suma")
            resultado= numero1 + numero2
        case "R":
            print("Restar")
            
            resultado= numero1 - numero2
        case "M":
            print("Multiplica")
            resultado= numero1 * numero2
        case "D":
            print("Dividir")
            resultado= numero1 / numero2
        case "E":
            control = False
        case _:
            print("Opción inválida.")
    print (f"Resultado={resultado}")