def mayor_ganancia(cant_dias, entrenamientos, energias):
    ganancias = [0]

    for i in range(cant_dias):
        for j in range(i):
            ganancias.append(max(ganancias))
            ganancias[j] = ganancias[j] + min(energias[i - j], entrenamientos[i])

    return max(ganancias)

def parsear_archivo(archivo):
    with open(archivo) as f:
        lineas = f.readlines()
        cant_dias = int(lineas[0])
        entrenamientos = [int(linea) for linea in lineas[1:cant_dias+1]]
        energias = [int(linea) for linea in lineas[cant_dias+1:]]
        return cant_dias, entrenamientos, energias
    
(cant_dias, entrenamientos, energias) = parsear_archivo("./test/5000.txt")
print(mayor_ganancia(len(entrenamientos), entrenamientos, energias)[0])
