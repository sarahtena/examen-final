import unittest
from estado_cuantico import EstadoCuantico

class TestEstadoCuantico(unittest.TestCase):
    def test_medicion_basica(self):
        estado = EstadoCuantico("test", [1, 0])
        probs = estado.medir()
        self.assertAlmostEqual(probs[0], 1.0)
        self.assertAlmostEqual(probs[1], 0.0)

    def test_estado_superposicion(self):
        estado = EstadoCuantico("psi", [0.7071, 0.7071])
        probs = estado.medir()
        self.assertAlmostEqual(probs[0], 0.5, places=2)
        self.assertAlmostEqual(probs[1], 0.5, places=2)
