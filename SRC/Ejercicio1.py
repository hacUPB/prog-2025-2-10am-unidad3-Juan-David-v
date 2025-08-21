print("Ingresa tu nombre y apellido")
nombre = input()
print("Bienvenido: ")
print(nombre)
#Opción 2
print("Bienvenido: ", nombre)
# calcular el IMC de esa persona
#Leer peso, altura
peso = input("Ingresar el peso en kg; ")
peso = float(peso)
altura = input("Ingresar tu altura en m; ")
altura = float(altura)
#Calculos

IMC = peso/altura**2
#Mostrar IMC
print("Tu IMC =", IMC)

if IMC >= 18.5 and IMC <= 24.9:
    print("Normal")
else:
    if IMC >= 25 and IMC <= 29.9:
        print("Sobrepeso")
    else:
        if IMC >= 30 and IMC <= 34.9:
            print("Sobrepeso I")
        else:
            if IMC >= 35 and IMC <= 39.9:
                print("Sobrepeso II")
            else:
                if IMC >= 40:
                    print("Sobrepeso II")