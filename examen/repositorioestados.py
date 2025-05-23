import json
import json
from estadocuantico import EstadoCuantico

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
        Devuelve una lista con las descripciones de todos los estados cuánticos almacenados en el repositorio.

        :return: Lista de descripciones de los estados, o mensaje indicando que no hay estados registrados.
        """
        if not self.estados:
            return ["No hay estados registrados"]
        
        return [str(estado) for estado in self.estados.values()]

    def agregar_estado(self, id, vector, base):
        """
        Crea un nuevo objeto EstadoCuantico a partir de los datos proporcionados y lo añade al repositorio.

        :param id: Identificador único del estado cuántico.
        :param vector: Vector que representa el estado cuántico.
        :param base: Base en la que se define el estado cuántico.
        :raises ValueError: Si el identificador ya existe en el repositorio.
        """
        if id in self.estados:
            raise ValueError(f"Error: ya existe un estado con identificador '{id}'")
        
        # Crear una nueva instancia de EstadoCuantico
        nuevo_estado = EstadoCuantico(id, vector, base)
        
        # Agregar el nuevo estado al repositorio
        self.estados[id] = nuevo_estado

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
    
    def aplicar_operador(self, id_estado, operador, nuevo_id=None):
        """
        Aplica un operador cuántico a un estado existente y registra el resultado.

        :param id_estado: Identificador del estado cuántico al que se aplicará el operador.
        :param operador: OperadorCuantico que se aplicará al estado.
        :param nuevo_id: Identificador para el nuevo estado resultante (opcional).
        :raises KeyError: Si el identificador del estado no existe en el repositorio.
        :raises ValueError: Si el nuevo identificador ya existe en el repositorio.
        :raises ValueError: Si las dimensiones del operador y el estado no coinciden.
        """
        # Obtener el estado cuántico original
        estado_original = self.obtener_estado(id_estado)

        # Validar que las dimensiones del operador coincidan con las del estado
        if len(estado_original.vector) != len(operador.matriz):
            raise ValueError("Las dimensiones del operador y el estado no coinciden.")

        # Aplicar el operador al estado original
        nuevo_vector = operador.aplicar(estado_original.vector)

        # Determinar el identificador del nuevo estado
        if nuevo_id:
            if nuevo_id in self.estados:
                raise ValueError(f"El estado con ID '{nuevo_id}' ya existe.")
            id_resultante = nuevo_id
        else:
            id_resultante = f"{id_estado}_{operador.nombre}"

        # Crear y registrar el nuevo estado
        self.agregar_estado(id_resultante, nuevo_vector, estado_original.base)

    def medir_estado(self, id_estado):
        """
        Mide el estado cuántico con el identificador dado y retorna las probabilidades de medición.

        :param id_estado: Identificador del estado cuántico a medir.
        :return: Diccionario con las probabilidades de medición.
        :raises KeyError: Si el identificador no existe en el repositorio.
        """
        # Obtener el estado cuántico
        estado = self.obtener_estado(id_estado)
        
        # Obtener las probabilidades de medición usando el método medir() de EstadoCuantico
        probabilidades = estado.medir()
        
        # Formatear las probabilidades en un mensaje entendible
        mensaje = f"Medición del estado '{id_estado}' en base {estado.base}:\n"
        for i, probabilidad in enumerate(probabilidades):
            mensaje += f"- Resultado {i}: {probabilidad * 100:.2f}%\n"
        
        print(mensaje)
        return probabilidades
    
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

    
    def __str__(self):
        """
        Representación en texto del repositorio, mostrando los identificadores de los estados.

        :return: Cadena que lista todos los identificadores de los estados.
        """
        return f"Repositorio de Estados: {', '.join(self.estados.keys())}"

    def __repr__(self):
        """
        Representación técnica del repositorio de estados.

        :return: Cadena que incluye los identificadores de los estados.
        """
        return f"RepositorioDeEstados(estados={list(self.estados.keys())})"

 

