import numpy as np
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
        nuevo_vector = np.array(estado.obtener_vector(), dtype=complex)
        return EstadoCuantico(nuevo_vector)

    def __repr__(self):
        return f"OperadorCuantico(nombre={self.nombre}, matriz_unitaria={self.matriz_unitaria})"


# Ejemplo de uso:
if __name__ == "__main__":
    # Definir el estado |0⟩
    estado_cero = EstadoCuantico([1, 0])

    # Definir la puerta X
    puerta_x = OperadorCuantico([[0, 1], [1, 0]], nombre="PuertaX")

    # Aplicar la puerta X al estado |0⟩
    estado_resultante = puerta_x.aplicar(estado_cero)

    print("Estado inicial:", estado_cero)
    print("Operador:", puerta_x)
    print("Estado resultante:", estado_resultante)