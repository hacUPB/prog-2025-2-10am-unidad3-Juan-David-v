'''
for cont in range (5, 20, 1):
    print(cont)
''' 
#Escribe un programa que solicite al usuario ingresar un número entero positivo n. 
# Luego, utiliza un bucle for con la función range() para calcular la suma de todos los números pares desde 1 hasta n. 
#Finalmente, muestra el resultado de la suma en pantalla.#

# No puede ingresar valores negativos y no se le permite seguir hasta que ingrese un positivo
'''
n = int(input("Ingresa un número entero positivo: "))
while n < 0:
    n = int(input("Ingresa un número entero positivo: "))
Suma = 0
for i in range (1, n + 1):
    if i % 2 == 0:
        Suma += i # acum= acum + cont# 
print("La suma de los números pares desde 1 hasta", n, "es:", Suma)
'''

mensaje = "Universidad Pontificia Bolivariana"
numero = int(input("Ingrese el numero entero positivo: "))
# imprimir el mensaje un numero de veces 

for i in range (numero):
    print (f"{i+1}. {mensaje}") 
