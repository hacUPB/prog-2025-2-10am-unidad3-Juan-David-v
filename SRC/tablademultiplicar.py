numero = int(input("Ingrese un número entero positivo: "))
while numero <= 0:
    print( " Error")
    numero = int(input("Ingrese un número entero positivo: "))
    print(f"Tabla de Multiplicar del {numero}:")
i = 1
while i <= 15:
    print(f"{numero} x {i} = {numero * i}")
    i += 1