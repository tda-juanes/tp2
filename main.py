# El formato de los sets de datos es: 
# En la primera línea el valor de la cantidad de días a considerar (n)
# En las siguientes n líneas, las ganancias de dichos días (nuestros e_i).
# En las siguientes n líneas, la energía con la que se cuenta al día 1, 2, 3, ..., n de estar entrenando sin haber descansando previamente (nuestros s_i).
# 
# Ejemplo 3.txt:
# 3  -> cantidad de días
# 1  -> ganancia día 1
# 5  -> ganancia día 2
# 4  -> ganancia día 3 
# 10 -> energía día 1 sin haber descansado previamente (es nuestro s1)
# 2  -> energía día 2 sin haber descansado previamente
# 2  -> energía día 2 sin haber descansado previamente
#
# Ganancia maxima: 7
# Plan de entrenamiento: Descanso, Entreno, Entreno

# 3
# energias = [10, 2, 2]
# entrenamientos = [
#     1, # Descanso  ganancia: 0 energía: 10
#     5, # Entreno   ganancia: 5 energía: 2
#     4  # Entreno   ganancia: 7 energía: 2
# ]

# 10 
energias = [
    63,
    61,
    49,
    41,
    40,
    38,
    23,
    17,
    13,
    10
]
entrenamientos = [
    36, # Entreno   ganancia:  36 energía: 61
    2,  # Descanso  ganancia:  36 energía: 63
    78, # Entreno   ganancia:  99 energía: 61
    19, # Descanso  ganancia:  99 energía: 63
    59, # Entreno   ganancia: 158 energía: 61
    76, # Entreno   ganancia: 219 energía: 49
    65, # Entreno   ganancia: 268 energía: 41
    64, # Entreno   ganancia: 309 energía: 40
    33, # Entreno   ganancia: 342 energía: 38
    41  # Entreno   ganancia: 380 energía: 23
]

def obtener_ganacia(entrenamiento, energia):
    return min(energia, entrenamiento)

def obtener_mejor_del_dia(entrenamientos):
    mejor = 0
    for entrenamiento in entrenamientos:
        if entrenamiento[0] > mejor:
            mejor = entrenamiento[0]
    return mejor

def mayor_ganancia(cant_dias, entrenamientos, energias):
    mejor_caso_dia = [[]] * cant_dias

    # el primer día es un caso base
    mejor_caso_dia[0] = [[obtener_ganacia(entrenamientos[0], energias[0]), 1]]

    # el segundo día tambien es un caso base (tal vez no sea necesario)
    mejor_caso_dia[1] = [
        [obtener_ganacia(entrenamientos[1], energias[0]), 1],
        [mejor_caso_dia[0][0][0] + obtener_ganacia(entrenamientos[1], energias[1]), 2]
    ]

    for i in range(2, cant_dias):
        casos_posibles = [
            [
                obtener_ganacia(entrenamientos[i], energias[0]) + obtener_mejor_del_dia(mejor_caso_dia[i-2]), 
                1 # dias consecutivos entrenados
            ],
        ]
        for caso_previo in mejor_caso_dia[i-1]:
            ganancia_previa = caso_previo[0]
            dias_consecutivos = caso_previo[1]
            caso = [
                    obtener_ganacia(entrenamientos[i], energias[dias_consecutivos]) + ganancia_previa,
                    dias_consecutivos+1
                    ]
            casos_posibles.append(caso)

        mejor_caso_dia[i] = casos_posibles

    return max(mejor_caso_dia[-1])

print(mayor_ganancia(len(entrenamientos), entrenamientos, energias))
