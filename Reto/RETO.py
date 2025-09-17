while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("A. Combustible y Velocidad")
    print("B.  Altitud y Ángulo de ataque")
    print("C. ")
    print("D. Salir")

    opcion = input("Selecciona una opción: ").upper()

    match opcion:
        case "A":
            print("\nCombustible y Velocidad")
          
            comb_inicial = float(input("Ingrese el combustible inicial: "))
            v_inicial = float(input("Ingrese la velocidad inicial: "))
            a = float(input("Ingrese la aceleración: "))
            resistencia_aire = float(input("Ingrese la resistencia del aire: "))
            

      
            comb_min = 100
            t = 5
            tiempo_max = 20
            consumo = 50  
                     
            comb_actual = comb_inicial
            velocidad = v_inicial
            v_objetivo = v_inicial
            MAX_I = tiempo_max // t
            
            
            consumo = consumo 
            tiempo = 0
            i = 0
            accion = ""

            while i < MAX_I and comb_actual > 0:

                if comb_actual <= comb_min:
                    v_objetivo = 400
                    accion = "Desacelerar - ALERTA: Combustible bajo"
                else:
                    v_objetivo = 500
                    accion = "Acelerar"

                if velocidad > v_objetivo:
                    velocidad = velocidad - (resistencia_aire * t)
                elif velocidad < v_objetivo:
                    velocidad = velocidad + (resistencia_aire * t)

                tiempo += t
                i += 1
                comb_actual -= consumo

                print(f"Iteración: {i}\n Tiempo: {tiempo} s\nCombustible: {comb_actual:} \n "
                      f"Velocidad: {velocidad:}\nAcción: {accion}")

            print("\n Calculo finalizado")
            print(f"Iteraciones: {i}")
            print(f"Tiempo total: {tiempo} segundos")
            print(f"Estado final = Velocidad: {velocidad:}\n Combustible: {comb_actual:}")








        case "B":
            print("\n Simulación de Altitud y Ángulo de ataque")
           
            altitud = float(input("Ingrese la altitud inicial: "))
            velocidad = float(input("Ingrese la velocidad inicial: "))
            angulo_ataque = float(input("Ingrese el ángulo de ataque inicial (entre -2 y 15): "))

            
            altitud_objetivo = 8000
            incremento_altitud = 100
            MAX_ITER = 20

            i = 0
            accion = ""

            while i < MAX_ITER:
                if altitud < altitud_objetivo:
                    accion = "Subir"
                    altitud = altitud + (velocidad * angulo_ataque * 0.01) + incremento_altitud
                    angulo_ataque += 1

                elif altitud > altitud_objetivo:
                    accion = "Bajar"
                    altitud = altitud - (velocidad * angulo_ataque * 0.01) - incremento_altitud
                    angulo_ataque -= 1

                else:
                    accion = "Mantener altitud"

                if angulo_ataque < -2:
                    angulo_ataque = -2
                if angulo_ataque > 15:
                    angulo_ataque = 15

                i += 1

                print(f"Iteración: {i} \n Altitud: {altitud:.2f}, Velocidad: {velocidad:.2f} "
                      f"\nÁngulo de ataque: {angulo_ataque}° \n Acción: {accion}")

            print("\n  Calculo finalizado")
            print(f"Iteraciones: {i}")
            print(f"Altitud final: {altitud:}\n Velocidad: {velocidad:.2f} "
                  f"\n Ángulo de ataque: {angulo_ataque}°")

        case "C":
            print("")

        case "D":
            print("")
            break
            

        case _:
            print("Opción inválida. Intente de nuevo.")

