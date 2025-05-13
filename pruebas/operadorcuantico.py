import unittest
from src.estado_cuantico import EstadoCuantico
from src.operador_cuantico import OperadorCuantico

class TestOperadorCuantico(unittest.TestCase):
    def test_aplicar_x_a_0(self):
        estado = EstadoCuantico("q0", [1, 0])
        X = OperadorCuantico("X", [[0, 1], [1, 0]])
        resultado = X.aplicar(estado)
        self.assertAlmostEqual(resultado.vector[0], 0.0)
        self.assertAlmostEqual(resultado.vector[1], 1.0)
