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
            

      
            comb_min = 500
            t = 5
            tiempo_max = 60
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
                    a += 5

                if velocidad >= v_objetivo:
                    a -= 5
                else:
                    a += 5
                
                velocidad = a * t -  (resistencia_aire * t)
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

                print(f"Iteración: {i} \n Altitud: {altitud:.2f}, Velocidad: {velocidad:.2f} \nÁngulo de ataque: {angulo_ataque}° \n Acción: {accion}")

        case "C":
            import math
            print("\n Tasa de descenso y flaps ")
            

            velocidad = float(input("Ingrese la velocidad inicial del avión (nudos): "))
            angulo_ataque = float(input("Ingrese el ángulo de ataque inicial (°): "))
            flaps = int(input("Ingrese la posición inicial de los flaps (°): "))

            MAX_ITER = 20
            D_CRITICO = 50
            A_CRITICO = 12
            FLAP_MIN = 0
            FLAP_MAX = 30
            i= 0

            while i < MAX_ITER and velocidad > 80:
                tasa_descenso = velocidad * math.sin(math.radians(angulo_ataque))
                if tasa_descenso > D_CRITICO:
                    nuevo_flap = flaps + 10
                    accion = "Aumentar flaps (ganar sustentación)"
                elif angulo_ataque > A_CRITICO:
                     nuevo_flap = flaps - 10
                     accion = "Reducir flaps (evitar pérdida)"
                else:
                    nuevo_flap = flaps
                    accion = "Mantener flaps"
                if nuevo_flap < FLAP_MIN:
                    nuevo_flap = FLAP_MIN
                if nuevo_flap > FLAP_MAX:
                    nuevo_flap = FLAP_MAX

                flaps = nuevo_flap
                if accion == "Aumentar flaps (ganar sustentación)":
                    angulo_ataque += 0.5
                elif accion == "Reducir flaps (evitar pérdida)":
                    angulo_ataque -= 0.5
                    if angulo_ataque < -5:
                        angulo_ataque = -5
                    if angulo_ataque > 18:
                        angulo_ataque = 18

                    perdida_vel = 5 + (flaps / 2)
                    velocidad -= perdida_vel
                    if velocidad < 0:
                        velocidad = 0


                    i += 1

                    print(f"Iteración: {i} \n Velocidad: {velocidad:} nudos \n Ángulo de ataque: {angulo_ataque}° \n Flaps: {flaps}° \n Tasa de descenso: {tasa_descenso:} \n Acción: {accion}")

                        




        case "D":
            print(" Salir")
            break
            

        case _:
            print("Opción inválida. Intente de nuevo.")

