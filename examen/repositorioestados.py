import json
import json

class RepositorioDeEstados:
    """
    Clase encargada de gestionar el conjunto de estados cuánticos registrados.
    """

    def __init__(self):
        """
        Inicializa el repositorio con un diccionario vacío para almacenar los estados cuánticos.
        """
        self.estados = {}

    def listar_estados(self):
        """
        Lista todos los estados cuánticos registrados con sus descripciones.

        :return: Una lista de strings descriptivos de los estados cuánticos.
        """
        return [f"ID: {id_estado}, Estado: {estado}" for id_estado, estado in self.estados.items()]

    def agregar_estado(self, id_estado, vector, base):
        """
        Crea un nuevo estado cuántico con los datos proporcionados y lo registra en el repositorio.

        :param id_estado: Identificador único del estado cuántico.
        :param vector: Vector que representa el estado cuántico.
        :param base: Base en la que se define el estado cuántico.
        :raises ValueError: Si el identificador ya existe en el repositorio.
        """
        if id_estado in self.estados:
            raise ValueError(f"El estado con ID '{id_estado}' ya existe.")
        
        # Crear un nuevo objeto EstadoCuantico
        estado_cuantico = EstadoCuantico(vector, base)
        
        # Registrar el estado cuántico en el repositorio
        self.estados[id_estado] = estado_cuantico

    def obtener_estado(self, id_estado):
        """
        Busca y retorna el estado cuántico con el identificador dado, en caso de ser necesario
        para otras operaciones (como aplicar operadores o medir).

        :param id_estado: Identificador del estado cuántico.
        :return: El objeto estado cuántico correspondiente.
        :raises KeyError: Si el identificador no existe en el repositorio.
        """
        estado = self.estados.get(id_estado)
        if estado is None:
            raise KeyError(f"El estado con ID '{id_estado}' no existe.")
        return estado
    
    def aplicar_operador(self, id_estado, op, nuevo_id=None):
        """
        Aplica un operador cuántico a un estado existente y registra el resultado.

        :param id_estado: Identificador del estado cuántico al que se aplicará el operador.
        :param op: OperadorCuantico que se aplicará al estado.
        :param nuevo_id: Identificador para el nuevo estado resultante (opcional).
        :raises KeyError: Si el identificador del estado no existe en el repositorio.
        :raises ValueError: Si el nuevo identificador ya existe en el repositorio.
        """
        # Obtener el estado cuántico original
        estado_original = self.obtener_estado(id_estado)

        # Aplicar el operador al estado original
        nuevo_vector = op.aplicar(estado_original.vector)

        # Determinar el identificador del nuevo estado
        if nuevo_id:
            if nuevo_id in self.estados:
                raise ValueError(f"El estado con ID '{nuevo_id}' ya existe.")
            id_resultante = nuevo_id
        else:
            id_resultante = f"{id_estado}_{op.nombre}"

        # Crear y registrar el nuevo estado
        self.agregar_estado(id_resultante, nuevo_vector, estado_original.base)

    def medir_estado(self, id_estado):
        """
        Mide el estado cuántico con el identificador dado y retorna sus probabilidades de medición.

        :param id_estado: Identificador del estado cuántico a medir.
        :return: Lista de probabilidades de medición.
        :raises KeyError: Si el identificador no existe en el repositorio.
        """
        # Obtener el estado cuántico
        estado = self.obtener_estado(id_estado)
        
        # Retornar las probabilidades de medición usando el método medir() de EstadoCuantico
        return estado.medir()
    
    def guardar(self, archivo):
        """
        Guarda la colección de estados cuánticos en un archivo JSON.

        :param archivo: Ruta del archivo donde se guardarán los estados.
        """
        with open(archivo, 'w') as f:
            estados_serializados = {
                id_estado: {
                    "vector": estado.vector,
                    "base": estado.base
                } for id_estado, estado in self.estados.items()
            }
            json.dump(estados_serializados, f, indent=4)

    def cargar(self, archivo):
        """
        Carga estados cuánticos desde un archivo JSON y los registra en el repositorio.

        :param archivo: Ruta del archivo desde donde se cargarán los estados.
        """
        with open(archivo, 'r') as f:
            estados_cargados = json.load(f)
            for id_estado, datos in estados_cargados.items():
                self.agregar_estado(id_estado, datos["vector"], datos["base"])

 

