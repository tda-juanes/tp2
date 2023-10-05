import sys
import time
from random import random

from main import maximizar_ganancias

'''
Receives a range of natural numbers and for each n in the range
outputs the time taken to process an input of length n.
Output has the following format:
"""
n_1,time_taken_1
n_2,time_taken_2
...
n_k,time_taken_k
"""
'''
def benchmark(rango):
    for cant_elementos in rango:
        entrenamientos = [random() for _ in range(cant_elementos)]
        energias = [random() for _ in range(cant_elementos)]
        energias.sort()
        timer_start = time.perf_counter()
        maximizar_ganancias(entrenamientos, energias)
        timer_end = time.perf_counter()
        print(f'{cant_elementos},{timer_end - timer_start}')

def main():
    if not 1 < len(sys.argv) < 5:
        print(
            'Usage:\n'
            'python3 benchmark.py STOP\n'
            'python3 benchmark.py START STOP\n'
            'python3 benchmark.py START STOP STEP\n'
            "Example: 'python3 benchmark.py 100000 1000001 100000'\n",
            file=sys.stderr
        )
        exit(1)
    rango = range(*map(int, sys.argv[1:]))
    benchmark(rango)

if __name__ == '__main__':
    main()