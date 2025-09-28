# Trabajo en casa


# Objetos, Variables y Etiquetas


# Creamos un objeto (en este caso, un número)
altitud = 10000  # metros

# 'altitud' es una etiqueta que apunta al objeto entero 10000
# Podemos crear otra etiqueta que apunte al mismo objeto
elevacion = altitud

# Si modificamos el valor al que apunta 'elevacion'
elevacion = 9500

# 'altitud' sigue apuntando al valor original
print(altitud)  # 10000
print(elevacion)  # 9500

# Aquí lo que se hizo es mostrar cómo funcionan las variables como etiquetas que apuntan a objetos en memoria en Python.
#El código demuestra que asignar una variable a otra no copia el objeto, solo copia la referencia. 
# Pero, si luego cambias una de las variables para que apunte a otro objeto, la otra se queda con el original.

velocidad = 800  # km/h
print(id(velocidad))  # Muestra el identificador único del objeto

otra_velocidad = 800
print(id(otra_velocidad))  # Para números pequeños, Python reutiliza objetos

lista1 = [1, 3, 67]
print(id(lista1))  # Muestra el identificador único del objeto lista

# Ejemplo con objetos inmutables (strings):

modelo = "Boeing 747"
print(id(modelo))  # Guardamos el ID original

# Intentamos "modificar" el string
modelo = modelo + "-800"
print(modelo)  # "Boeing 747-800"
print(id(modelo))  # ¡ID diferente! Se creó un nuevo objeto



 # MUTABLES E INMUTABLES 


# Ejemplo con objetos mutables (listas):
componentes = ["alas", "fuselaje", "motores"]
print(id(componentes))  # Guardamos el ID original

# Modificamos la lista
componentes.append("tren de aterrizaje")
print(componentes)  # ["alas", "fuselaje", "motores", "tren de aterrizaje"]
print(id(componentes))  # Mismo ID, el objeto fue modificado in-place

#Cómo afecta la mutabilidad a los objetos que se usan como argumentos de una función?
def agregar_combustible(tanques, litros):
    tanques.append(litros)
    print(f"Combustible actualizado: {tanques}")

combustible_actual = [1000, 1200, 800]  # Lista (objeto mutable)
agregar_combustible(combustible_actual, 500)
print(combustible_actual)  # [1000, 1200, 800, 500] - La lista original fue modificada

#Si el argumento es mutable (listas, diccionarios, sets, etc.), los cambios hechos dentro de la función afectan al objeto original.

#Si el argumento es inmutable (enteros, floats, strings, tuplas, etc.), no se puede modificar el objeto, y cualquier “cambio” crea un objeto nuevo sin alterar el original.

# ITERABLES E INTERACION 
# ITERABLES CON BUCLE FOR 

# Iterando sobre una lista de sensores de aeronave
sensores = ["temperatura", "presión", "velocidad", "altitud", "combustible"]

for sensor in sensores:
    print(f"Comprobando sensor de {sensor}...")

## Iterando sobre una lista de sensores de aeronave
sensores = ["temperatura", "presión", "velocidad", "altitud", "combustible"]

for sensor in sensores:
    print(f"Comprobando sensor de {sensor}...")

# Simulando lecturas de altitud cada 10 segundos
altitudes = [0, 100, 500, 1000, 1500, 2000, 2200, 2500]
tiempo = 0
i = 0

while i < len(altitudes):
    print(f"Tiempo: {tiempo}s - Altitud: {altitudes[i]} metros")
    tiempo += 10
    i += 1

###Funciones de iteración útiles

# enumerate(): Proporciona índices junto con valores

for i, etapa in enumerate(["despegue", "ascenso", "crucero", "descenso", "aterrizaje"]):
    print(f"Etapa {i+1}: {etapa}")

#zip(): Combina dos o más iterables
tiempos = [0, 10, 20, 30]
velocidades = [0, 200, 300, 320]

for t, v in zip(tiempos, velocidades):
    print(f"Tiempo: {t}s - Velocidad: {v} km/h")
