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

