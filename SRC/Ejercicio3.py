#Condicional Simple: 
#Se le pide al usuario que ingrese un numero entero y que muestre un mensaje si el numero es divisible por 3.
 
numero = int(input("Ingresar el numero; "))

residuo=( numero % 3)

if residuo == 0:
    print(f"{numero}, es divisible en 3")



#Condicional Doble: 
print("=== MENÚ PRINCIPAL ===")
print("A. Ver datos de sensores")
print("B. Configurar parámetros")
print("C. Salir")

opcion = int(input("Selecciona una opción: "))

match opcion:
    case "A":
        print("Mostrando datos de sensores...")
    case "B":
        print("Entrando a configuración...")
    case "C":
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")


