import sys

def calcular_ganancias(entrenamientos, energias):
    ganancias = [0]

    for dia_actual in range(len(entrenamientos)):
        ganancias.append(max(ganancias))
        for i in range(dia_actual + 1):
            ganancias[i] = ganancias[i] + min(energias[dia_actual - i], entrenamientos[dia_actual])

    return ganancias


def reconstruir_solucion(ganancias, entrenamientos, energias):
    dia_actual = len(entrenamientos) - 1
    solucion = [True] * (dia_actual + 1)
    while dia_actual > 0:
        idx_max = ganancias.index(max(ganancias[:dia_actual]))
        solucion[idx_max - 1] = False
        for i in range(dia_actual, idx_max - 1, -1):
            for j in range(idx_max - 1, -1, -1):
                ganancias[i] -= min(entrenamientos[i], energias[i - j])
        dia_actual = idx_max - 1
    return reversed(solucion)


def parse_input(file_h):
    try:
        cant_lineas = int(file_h.readline())
        input_lines = [int(line) for line in file_h]
        entrenamientos = input_lines[:cant_lineas]
        energias = input_lines[cant_lineas:]
        assert cant_lineas == len(entrenamientos) == len(energias)
        return entrenamientos, energias
    except ValueError:
        print('Invalid input: Line contents must be valid integers', file=sys.stderr)


def main():
    entrenamientos, energias = parse_input(sys.stdin)
    ganancias = calcular_ganancias(entrenamientos, energias)
    print('Ganancia maxima:', max(ganancias))
    solucion = reconstruir_solucion(ganancias, entrenamientos, energias)
    mapping = {True: 'Entreno', False: 'Descanso'}
    print('Plan de entrenamiento:', ', '.join(map(mapping.get, solucion)))

if __name__ == '__main__':
    main()
