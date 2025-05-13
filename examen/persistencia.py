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

