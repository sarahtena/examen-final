import unittest
import tempfile
import os
from src.estado_cuantico import EstadoCuantico
from src.repositorio import RepositorioDeEstados

class TestPersistencia(unittest.TestCase):
    def test_guardar_y_cargar(self):
        repo = RepositorioDeEstados()
        repo.agregar_estado(EstadoCuantico("q0", [1, 0]))
        repo.agregar_estado(EstadoCuantico("q1", [0, 1]))

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            nombre_archivo = tmp.name
        try:
            repo.guardar(nombre_archivo)
            repo.estados.clear()
            self.assertEqual(len(repo.estados), 0)
            repo.cargar(nombre_archivo)
            self.assertIn("q0", repo.estados)
            self.assertIn("q1", repo.estados)
        finally:
            os.remove(nombre_archivo)
