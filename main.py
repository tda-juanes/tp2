import sys

def mayor_ganancia(entrenamientos, energias):
    ganancias = [0]

    for i in range(len(entrenamientos)):
        ganancias.append(max(ganancias))
        for j in range(i):
            ganancias[j] = ganancias[j] + min(energias[i - j], entrenamientos[i])

    return max(ganancias)


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


if __name__ == '__main__':
    print(mayor_ganancia(*parse_input(sys.stdin)))
