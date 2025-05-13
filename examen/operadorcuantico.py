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
        Aplica el operador cuántico al estado dado.

        :param estado: Instancia de la clase EstadoCuantico sobre la que se aplica el operador.
        :return: Un nuevo objeto EstadoCuantico con el estado transformado.
        """
        # Verificamos que el estado tenga la dimensión correcta
        if len(estado.vector_estado) != self.matriz.shape[0]:
            raise ValueError(f"La dimensión del operador {self.nombre} no coincide con la del estado.")

        # Multiplicamos la matriz por el vector de amplitudes del estado
        nuevo_vector = np.dot(self.matriz, estado.vector_estado)

        # Creamos un nuevo estado cuántico con el vector transformado
        nuevo_estado = EstadoCuantico(estado.identificador + "_" + self.nombre, nuevo_vector.tolist(), estado.base)
        
        return nuevo_estado

    def __repr__(self):
        return f"OperadorCuantico(nombre={self.nombre}, matriz={self.matriz})"


