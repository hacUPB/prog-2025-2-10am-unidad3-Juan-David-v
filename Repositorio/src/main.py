'''
import Modulos
# funcion principal
numero = int(input("Ingrese un numero entero mayor que 1: "))
Modulos.identificadorprimos(numero)
variable = int(input("ingrese el numero de terminos de la serie de fibonacci"))
Modulos.fibonacci(variable)
multiplicando = int(input("ingrese el numero entero: "))
Modulos.tabla(multiplicando)
'''
from modulo.Modulos import * # * significa todo
 
def main():
   while True:
       opc = menu()
       match opc: 
           case 1:
               print("Calcular si un numero es primo.")
               valor = int (input(" ingresa un numero entero mayor que 1 >> "))
               primo(valor)
           case 2:
               print("Imprime la serie de fibonacci.")
               num = int (input(" ingresa un numero de terminos >> "))
               fibonacci(num)
           case 3: 
               print("Imprime la tabla de multiplicar.")
               valor = int (input(" ingresa el numero>> "))
               tabla(valor)
           case 4:
               break
           case _:
               print("La opcion que ingreso no es valida.")





if __name__ == "__main__":
    main()


