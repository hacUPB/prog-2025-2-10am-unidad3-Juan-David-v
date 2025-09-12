#Pseudocodigo combustible
Durante un vuelo, la velocidad de un avión depende de la aceleración aplicada por los motores, de la resistencia del aire y de la cantidad de combustible disponible.
El avión parte con una velocidad inicial de 500 km/h y un nivel de combustible definido por el usuario.
Cada 5 segundos el sistema descuenta 5 galones de combustible y actualiza la velocidad aplicando la fórmula
La simulación continúa hasta que el combustible se agote o se cumpla un tiempo máximo de 1 hora de vuelo.

| Tipo de variable | Nombre           | Descripción                                            | Unidad          |
|------------------|------------------|--------------------------------------------------------|-----------------|
| **Entrada**        | comb_inicial   | Combustible inicial                                    | galones         |
|                  | v_inicial        | Velocidad inicial                                      | km/h            |
|                  | a                | Aceleración                                            | km/h²           |
|                  | resistencia_aire | Factor de resistencia del aire                        | km/h²           |
| **Constante**    | comb_min         | Nivel mínimo de combustible seguro (= 100)            | galones         |
|                  | t               | Intervalo de tiempo por iteración                      | 5 segundos      |
|                  | tiempo_max       | Tiempo máximo de simulación                            | 3600 segundos   |
| **Control**      | i             | Número de iteraciones                                  | -               |
|                  | tiempo           | Tiempo acumulado                                       | segundos        |
| **Salida**       | velocidad        | Velocidad actual del avión                             | km/h            |
|                  | comb_actual      | Combustible restante                                   | galones         |
|                  | v_objetivo       | Velocidad objetivo (400 o 500 según condición)         | km/h            |
|                  | accion           | Acción tomada (acelerar, mantener, alerta)             | texto           |

```
Inicio
 Leer comb_inicial =
    Leer v_inicial =
    Leer a =
    Leer resistencia_aire =

    comb_min = 100          // Combustible mínimo seguro
    t = 5                  // Intervalo de tiempo (5 segundos)
    tiempo_max = 3600       // Tiempo máximo de simulación (1 hora)

    
   comb_actual = comb_inicial
   velocidad = v_inicial
   v_objetivo = v_inicial
   tiempo = 0
   i = 0
   accion = ""

    
   Mientras (tiempo < tiempo_max and comb_actual > 0) Hacer

        Si comb_actual <= comb_min:
            v_objetivo = 400
            accion = " Desacelerar - ALERTA: Combustible bajo"
        Sino 
            v_objetivo = 500
            Accion = "Acelerar"
        Fin Si
    SI (velocidad > v_objetivo) 
            velocidad = velocidad - (resistencia_aire * dt)
        Si no
             Si (velocidad < v_objetivo)
            velocidad = velocidad + (aceleracion * dt)
        Fin Si

    tiempo = tiempo + t
    i = i + 1
    comb_actual= comb_actual - consumo

Imprimir ("Iteración:", iter, " Tiempo:", tiempo, " Combustible:", comb_actual, "Velocidad:", velocidad,  " Acción:", accion)

    Fin mientras
    Imprimir( ("Simulación finalizada");("Iteraciones:", i);("Tiempo total:", tiempo)
     ("Estado final= Velocidad:"), velocidad, " (Combustible:", comb_actual))
```











#Pseudocodigo altitud
#Un avión debe estabilizarse cerca de una altitud de 8000 pies con un margen de error de ±200 pies.
#Si la altitud actual está por debajo del rango permitido, el avión debe subir en incrementos de 100 ft.
#Si está por encima, debe bajar en decrementos de 100 ft.
#Cuando se encuentre dentro del rango permitido, el avión debe mantener la altitud.
#El sistema debe mostrar en cada iteración la altitud actual, la acción realizada y la cantidad de iteraciones.

'''
Inicio
    Leer alt_actual         // Altitud inicial del avión (ft)
    alt_objetivo = 8000     // Altitud deseada (ft)
    Leer alt_max            // Margen permitido (ej: 200 ft)
    movimiento = ""         // Inicializa movimiento
    Control = 0             // Variable de control
    Max_iter = 200          // Límite de iteraciones
 
    Mientras (abs(alt_actual - alt_objetivo) > alt_max) Y (Control < Max_iter) Hacer
        Si alt_actual < (alt_objetivo - alt_max) Entonces
            movimiento = "Subir"
            alt_actual = alt_actual + 100
        Sino Si alt_actual > (alt_objetivo + alt_max) Entonces
            movimiento = "Bajar"
            alt_actual = alt_actual - 100
        FinSi
 
        Control = Control + 1
        Imprimir "Iteración: ", Control, 
                 " Altitud actual: ", alt_actual, " ft", 
                 " Movimiento: ", movimiento
    FinMientras
 
    movimiento = "Mantener estable"
    Imprimir "Altitud final cercana a ", alt_objetivo, " ft. Estado: ", movimiento
Fin
'''


#Pseudocodigo peso.
#Antes de despegar, una aerolínea debe asegurarse de que el peso total del avión no exceda el peso máximo autorizado.
#El sistema recibe como datos el peso vacío de la aeronave, el peso del combustible cargado y el peso de la carga.
#Con estos valores:
#Se calcula el peso total.
#Si no coincide con el peso máximo permitido, se realizan ajustes en incrementos de 1 kg hasta alcanzar el límite exacto.
#En cada ajuste se imprime el valor del peso y el número de iteración
'''
Inicio
    Leer Peso_vacio      // Peso vacío de la aeronave (kg)
    Leer Peso_comb       // Peso del combustible (kg)
    Leer Peso_carga      // Peso de la carga (kg)
    Leer Peso_max        // Peso máximo autorizado (kg)
 
    Paso = 1             // Cantidad de peso a ajustar en cada iteración (kg)
    Control = 0          // Variable de control
    Max_iter = 1000      // Límite de seguridad para detener el ciclo
 
    Peso_total = Peso_vacio + Peso_comb + Peso_carga
 
    Mientras (Peso_total ≠ Peso_max) Y (Control < Max_iter) Hacer
        Si Peso_total < Peso_max Entonces
            Peso_total = Peso_total + Paso
        Sino
            Peso_total = Peso_total - Paso
        FinSi
        Control = Control + 1
        Imprimir "Iteración: ", Control, " Peso total: ", Peso_total, " kg"
    FinMientras
 
    Imprimir "Peso total ajustado: ", Peso_total, " kg"
Fin
'''

# DECLARACION IA
# Para complementar y organizar mejor las ideas en la construcción de los pseudocódigos, utilizamos una herramienta de inteligencia artificial como apoyo. 
# Esta se usó únicamente como guía, pero la comprensión, adaptación y explicación  del trabajo son de nuestra autoria 