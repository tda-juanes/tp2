def maximizar_ganancias(entrenamientos, energias):
    ganancias = [0]

    for dia_actual in range(len(entrenamientos)):
        ganancias.append(max(ganancias))
        for i in range(dia_actual + 1):
            ganancias[i] += min(energias[dia_actual-i], entrenamientos[dia_actual])

    return max(ganancias)
