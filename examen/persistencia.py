import json
from estadocuantico import EstadoCuantico  
def guardar_estados_json(estados: dict, archivo: str):
    estados_json = [
        {'id': e.id, 'vector_amplitudes': e.vector_amplitudes.tolist()}
        for e in estados.values()
    ]
    with open(archivo, 'w') as f:
        json.dump(estados_json, f, indent=4)

def cargar_estados_json(archivo: str) -> dict:
    estados = {}
    with open(archivo, 'r') as f:
        estados_json = json.load(f)
        for e in estados_json:
            estado = EstadoCuantico(e['id'], e['vector_amplitudes'])
            estados[estado.id] = estado
    return estados
