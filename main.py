energia_inicial = 5
entrenamientos = [1,2,3,4,5,6]

# En el caso planteado el mejor entrenamiento posible es:
# hago 1       ( 1, 4)
# hago 2       ( 3, 2)
# no hago 3    ( 3, 5)
# hago 4       ( 7, 1)
# no hago 5    ( 7, 5)
# hago 6       (12, 0)

def obtener_ganancia(energia_disponible, entrenamiento):
    ganancia = (min(energia_disponible, entrenamiento))
    energia_restante = energia_disponible - ganancia
    return (ganancia, energia_restante)

def mayor_ganancia(energia_inicial, entrenamientos):
    # La ganancia inicial (minima) de cada entrenamiento es hacerlo por si solo
    ganancias = [obtener_ganancia(energia_inicial, entrenamiento) for entrenamiento in entrenamientos]
    for i in range(len(entrenamientos)):
        # Casos bases, primer y segundo entrenamiento
        if i == 0: 
            # Nada que hacer, el mejor caso es su inicial
            continue
        if i == 1:
            # El segundo entrenamiento no se suma a nada anterior
            c1 = ganancias[i]
            g = obtener_ganancia(ganancias[i-1][1], entrenamientos[i])
            c2 = (ganancias[i-1][0]+g[0], g[1])
            ganancias[i] = max(c1, c2)
            continue

        # Dos escenarios posibles
        # c1: entrenar habiendo descansado el día anterior
        c1 = (ganancias[i-2][0] + ganancias[i][0], ganancias[i][1])
        # c2: entrenar no habiendo descansado el día anterior
        g = obtener_ganancia(ganancias[i-1][1], entrenamientos[i])
        c2 = (ganancias[i-1][0] + g[0], g[1])
        ganancias[i] = max(c1, c2)
    return max(ganancias)

print(mayor_ganancia(energia_inicial, entrenamientos))

