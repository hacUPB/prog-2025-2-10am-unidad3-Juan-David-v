def suma(a, b):
	resultado = a + b
	return resultado

def resta(num1,num2):
	resultado = num1- num2
	return resultado

def max(num1, num2):
	if num1 > num2:
		maximo = num1
	else:
		maximo= num2
	return maximo 

# seccion para el programa principal
#Llamando a la función
numero1 = 5
numero2 = 3
# Las variables pertenecen al contexto donde fueron creadas
a = 1000
b = 500
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898,564))
suma(45, 78)

res_resta = resta(a, b)
print(res_resta)

texto = " La universidad pontificia bolivariana se encuentra en el barrio laureles de medellin"
x = texto.find("laureles")

print= (x)