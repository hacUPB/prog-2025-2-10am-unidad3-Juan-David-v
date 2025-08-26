#Condicional Simple: 
#Se le pide al usuario que ingrese un numero entero y que muestre un mensaje si el numero es divisible por 3.
 
numero = int(input("Ingresar el numero; "))

residuo=( numero % 3)

if residuo == 0:
    print(f"{numero}, es divisible en 3")



#Condicional Doble: 
print("=== MENÚ PRINCIPAL ===")
print("1. Ver datos de sensores")
print("2. Configurar parámetros")
print("3. Salir")

opcion = int(input("Selecciona una opción: "))

match opcion:
    case 1:
        print("Mostrando datos de sensores...")
    case 2:
        print("Entrando a configuración...")
    case 3:
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")


