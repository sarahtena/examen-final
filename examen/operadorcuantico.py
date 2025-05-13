import numpy as np
from typing import Union
from estadocuantico import EstadoCuantico

class OperadorCuantico:
    def __init__(self, nombre: str, matriz: Union[list[list[complex]], np.ndarray]):
        """
        Representa un operador cuántico como una matriz unitaria.
        :param matriz_unitaria: numpy.ndarray que representa la matriz unitaria.
        :param nombre: Nombre o identificador del operador.
        """
        self.matriz = np.array(matriz, dtype=complex)
        self.nombre = nombre
        if self.matriz.shape[0] != self.matriz.shape[1]:
            raise ValueError("La matriz del operador debe ser cuadrada.")

        # Verificar que la matriz es unitaria
        if not np.allclose(self.matriz_unitaria @ self.matriz_unitaria.conj().T, np.eye(self.matriz_unitaria.shape[0])):
            raise ValueError("La matriz proporcionada no es unitaria.")

    def aplicar(self, estado):
        """
        Aplica el operador cuántico a un estado cuántico.
        :param estado: Objeto EstadoCuantico al que se aplicará el operador.
        :return: Nuevo objeto EstadoCuantico resultante.
        """
    def aplicar(self, estado: EstadoCuantico) -> EstadoCuantico:
        """
        Aplica el operador cuántico a un estado cuántico.
        :param estado: Objeto EstadoCuantico al que se aplicará el operador.
        :return: Nuevo objeto EstadoCuantico resultante.
        """
        nuevo_vector = estado.vector  # Asumimos que EstadoCuantico tiene un atributo 'vector'
        if len(nuevo_vector) != self.matriz.shape[1]:
            raise ValueError("La dimensión del vector de estado no coincide con la del operador.")
        return EstadoCuantico(self.matriz @ nuevo_vector)

    def __repr__(self):
        return f"OperadorCuantico(nombre={self.nombre}, matriz={self.matriz})"


