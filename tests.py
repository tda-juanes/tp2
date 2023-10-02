import unittest
from main import maximizar_ganancias, reconstruir_solucion

def solucion(entrenamientos, energias):
    ganancias = maximizar_ganancias(entrenamientos, energias)
    return reconstruir_solucion(ganancias, entrenamientos, energias)

def calcular_ganancia(solucion, entrenamientos, energias):
    ganancia_total = i = 0
    for entreno, ganancia in zip(solucion, entrenamientos):
        if entreno:
            ganancia_total += min(ganancia, energias[i])
            i += 1
        else:
            i = 0
    return ganancia_total


class TestCronograma(unittest.TestCase):
    def test_empty(self):
        got = solucion([], [])
        expected = []
        self.assertSequenceEqual(got, expected)

    def test_one(self):
        got = solucion([5], [6])
        expected = [True]
        self.assertSequenceEqual(got, expected)

    def test_todo_entreno(self):
        entrenamientos = [100, 90, 100, 90, 100, 90, 100, 90, 100, 90]
        energias       = [90, 100, 90, 100, 90, 100, 90, 100, 90, 100]
        got = solucion(entrenamientos, energias)
        self.assertTrue(all(got))

    def test_reconstruir(self):
        entrenamientos = [36,  2, 78, 19, 59, 76, 65, 64, 33, 41]
        energias       = [63, 61, 49, 41, 40, 38, 23, 17, 13, 10]
        ganancias = maximizar_ganancias(entrenamientos, energias)
        expected = max(ganancias)
        solucion = reconstruir_solucion(ganancias, entrenamientos, energias)
        got = calcular_ganancia(solucion, entrenamientos, energias)
        self.assertEqual(got, expected)

if __name__ == '__main__':
    unittest.main()
