'''
Variables de entrada
Nombre       Tipo
opcion       str
temperatura  float

Variables de salida
Nombre       Tipo
conversion   float

Variables de control
opcion
'''

opcion= "Z"         #Asigno un valor diferente de Q
while opcion != "Q":
    opcion = input("F. Fahrenheit a Celsius\nC. Celcius a Fahrenhiet\nQ. Salir\n")
    opcion = opcion.upper()
    if  opcion != "Q":
        temperatura = float(input("ingrese la temperatura a convertir: "))
    match opcion:
        case "F":
            conversion = (temperatura-32)*(5/9)
            print(f"{temperatura}°F = {conversion}°C")
        case "c":
            conversion = (temperatura * 9/5) + 32
            print(f"{temperatura}°C = {conversion}°f")
        case "Q":
            print("saliendo del programa")
        case _:
            print("opcion no valida")
else:
    print("Saliendo del Programa...")
