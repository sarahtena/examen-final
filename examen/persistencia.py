import json
from estadocuantico import EstadoCuantico  

def guardar_estados_json(estados: dict, archivo: str):
    """
    Guarda los estados cuánticos en un archivo JSON.
    Cada estado se representa con campos: id, base, vector.
    """
    lista_estados = []
    for estado in estados.values():
        lista_estados.append({
            "id": estado.id,
            "base": estado.base,
            "vector": estado.vector.tolist() if hasattr(estado.vector, 'tolist') else estado.vector
        })

    with open(archivo, 'w') as file:
        json.dump(lista_estados, file, indent=4)

def cargar_estados_json(archivo: str) -> dict:
    """
    Carga los estados cuánticos desde un archivo JSON y los devuelve en un diccionario.
    """
    estados = {}
    with open(archivo, 'r') as f:
        estados_json = json.load(f)
        for e in estados_json:
            estado = EstadoCuantico(e['id'], e['vector'], base=e.get('base', 'computacional'))
            estados[estado.id] = estado
    return estados

def guardar(self, archivo: str):
        """
        Guarda todos los estados cuánticos en un archivo JSON.
        Maneja errores de escritura (permiso, disco lleno, etc.).
        """
        try:
            lista_estados = []
            for estado in self.estados.values():
                lista_estados.append({
                    "id": estado.id,
                    "base": estado.base,
                    "vector": estado.vector.tolist() if hasattr(estado.vector, 'tolist') else estado.vector
                })
            with open(archivo, mode='w') as file:
                json.dump(lista_estados, file, indent=4)
        except Exception as e:
            print(f"Error al guardar estados en el archivo '{archivo}': {e}")

def cargar(self, archivo: str):
        """
        Carga estados cuánticos desde un archivo JSON.
        Si ya hay estados en memoria, los reemplaza.
        Asume formato correcto pero maneja archivo no encontrado.
        """
        try:
            with open(archivo, 'r') as file:
                lista_estados = json.load(file)
                self.estados.clear()  # Limpiar estados actuales antes de cargar
                for e in lista_estados:
                    estado = EstadoCuantico(e['id'], e['vector'], base=e.get('base', 'computacional'))
                    self.agregar_estado(estado)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo}")
        except json.JSONDecodeError:
            print(f"Error al interpretar el contenido del archivo JSON: {archivo}")
        except Exception as e:
            print(f"Ocurrió un error al cargar los estados desde el archivo '{archivo}': {e}")

