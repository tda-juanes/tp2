def obtener_ganacia(entrenamiento, energia):
    return min(energia, entrenamiento)

def obtener_mejor_del_dia(entrenamientos):
    mejor = entrenamientos[0]
    for entrenamiento in entrenamientos:
        if entrenamiento[0] > mejor[0]:
            mejor = entrenamiento
    return mejor

def mayor_ganancia(cant_dias, entrenamientos, energias):
    # el primer día es un caso base
    mejor_caso_dia_ant_a_prev = [obtener_ganacia(entrenamientos[0], energias[0]), 1]

    # el segundo día tambien es un caso base (tal vez no sea necesario)
    casos_dia_anterior = [
        [obtener_ganacia(entrenamientos[1], energias[0]), 1],
        [mejor_caso_dia_ant_a_prev[0] + obtener_ganacia(entrenamientos[1], energias[1]), 2]
    ]

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
            dias_consecutivos = caso_previo[1]
            caso = [
                    obtener_ganacia(entrenamientos[i], energias[dias_consecutivos]) + ganancia_previa,
                    dias_consecutivos+1
                    ]
            casos_posibles_dia_actual.append(caso)

        mejor_caso_dia_ant_a_prev = obtener_mejor_del_dia(casos_dia_anterior)
        casos_dia_anterior = casos_posibles_dia_actual

    return max(casos_dia_anterior)


def parsear_archivo(archivo):
    with open(archivo) as f:
        lineas = f.readlines()
        cant_dias = int(lineas[0])
        entrenamientos = [int(linea) for linea in lineas[1:cant_dias+1]]
        energias = [int(linea) for linea in lineas[cant_dias+1:]]
        return cant_dias, entrenamientos, energias
    
(cant_dias, entrenamientos, energias) = parsear_archivo("./test/10.txt")
print(mayor_ganancia(len(entrenamientos), entrenamientos, energias)[0])
