def obtener_ganacia(entrenamiento, energia):
    return min(energia, entrenamiento)

def mayor_ganancia(cant_dias, entrenamientos, energias):
    # el primer día es un caso base
    mejor_caso_dia_ant_a_prev = [obtener_ganacia(entrenamientos[0], energias[0]), 1]

    # el segundo día tambien es un caso base
    casos_dia_anterior = []
    ganancia_con_descanso = obtener_ganacia(entrenamientos[1], energias[0])
    ganancia_sin_descanso = mejor_caso_dia_ant_a_prev[0] + obtener_ganacia(entrenamientos[1], energias[1])
    if ganancia_con_descanso > ganancia_sin_descanso:
        casos_dia_anterior = [[ganancia_con_descanso, 1], [ganancia_sin_descanso, 2]]
    else:
        casos_dia_anterior = [[ganancia_sin_descanso, 2], [ganancia_con_descanso, 1]]

    for i in range(2, cant_dias):
        # caso descanse el dia anterior
        casos_posibles_dia_actual = [
            [
                obtener_ganacia(entrenamientos[i], energias[0]) + mejor_caso_dia_ant_a_prev[0], 
                1 # dias consecutivos entrenados
            ],
        ]
        # demas casos
        for caso_previo in casos_dia_anterior:
            ganancia_previa = caso_previo[0]
            ganancia_nueva = obtener_ganacia(entrenamientos[i], energias[caso_previo[1]]) + ganancia_previa
            dias_consecutivos = caso_previo[1]
            caso = [ganancia_nueva, dias_consecutivos+1]

            if ganancia_nueva > casos_posibles_dia_actual[0][0]:
                casos_posibles_dia_actual.insert(0, caso) # si es mejor que el mejor caso actual, lo inserto al principio
            else: 
                casos_posibles_dia_actual.append(caso) # si no, lo inserto al final

        mejor_caso_dia_ant_a_prev = casos_dia_anterior[0]
        casos_dia_anterior = casos_posibles_dia_actual

    return casos_dia_anterior[0]


def parsear_archivo(archivo):
    with open(archivo) as f:
        lineas = f.readlines()
        cant_dias = int(lineas[0])
        entrenamientos = [int(linea) for linea in lineas[1:cant_dias+1]]
        energias = [int(linea) for linea in lineas[cant_dias+1:]]
        return cant_dias, entrenamientos, energias
    
(cant_dias, entrenamientos, energias) = parsear_archivo("./test/5000.txt")
print(mayor_ganancia(len(entrenamientos), entrenamientos, energias)[0])
