from typing import List, Union
class EstadoCuantico:
    def __init__(self, identificador: str, vector_estado: List[Union[float, complex]], base: str = "computacional"):
        """
        Inicializa un estado cuántico.

        :param identificador: Nombre o etiqueta única del estado.
        :param vector_estado: Lista de amplitudes (floats o números complejos).
        :param base: Base en la que está expresado el vector (por defecto "computacional").
        """
        if not vector_estado:
            raise ValueError("El vector de estado no puede estar vacío.")
        self.identificador = identificador
        self.vector_estado = [complex(x) for x in vector_estado]
        self.base = base

    def medir(self):
        """
        Calcula las probabilidades de resultados de medición a partir del vector de estado.

        :return: Lista de probabilidades (|amplitud|^2 para cada componente).
        """
        return [abs(amplitud)**2 for amplitud in self.vector_estado]

    def __str__(self):
        """
        Representación en texto del estado cuántico.

        :return: Cadena con el identificador, vector de estado y base.
        """
        return f"{self.identificador}: {self.vector_estado} en base {self.base}"

    def __repr__(self):
        """
        Representación técnica del estado cuántico.

        :return: Cadena con el identificador, vector de estado y base.
        """
        return f"EstadoCuantico(identificador={self.identificador}, vector_estado={self.vector_estado}, base={self.base})"

    def obtener_vector(self):
        """
        Devuelve el vector de estado.

        :return: Lista de amplitudes del vector de estado.
        """
        return self.vector_estado

    def obtener_base(self):
        """
        Devuelve la base del estado cuántico.

        :return: Base en la que está expresado el vector.
        """
        return self.base

    def obtener_identificador(self):
        """
        Devuelve el identificador del estado cuántico.

        :return: Identificador del estado.
        """
        return self.identificador
    
    def _esta_normalizado(self):
        """
        Verifica si el vector de estado está normalizado, es decir, la suma de los cuadrados de
        las amplitudes debe ser igual a 1 (con una tolerancia numérica).
        """
        suma_cuadrados = sum(abs(amplitud)**2 for amplitud in self.vector_estado)
        return cmath.isclose(suma_cuadrados, 1.0)
    

