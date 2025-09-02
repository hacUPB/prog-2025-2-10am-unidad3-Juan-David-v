'''
for cont in range (5, 20, 1):
    print(cont)
''' 
#Escribe un programa que solicite al usuario ingresar un número entero positivo n. 
# Luego, utiliza un bucle for con la función range() para calcular la suma de todos los números pares desde 1 hasta n. 
#Finalmente, muestra el resultado de la suma en pantalla.#

n = int(input("Ingresa un número entero positivo: "))
Suma = 0
for i in range (1, n + 1):
    if i % 2 == 0:
        Suma += i # acum= acum + cont# 
print("La suma de los números pares desde 1 hasta", n, "es:", Suma)