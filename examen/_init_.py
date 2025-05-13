# src/ejecutar.py
from estadocuantico import EstadoCuantico
from operadorcuantico import OperadorCuantico
from repositorioestados import RepositorioDeEstados

def ejecutar_programa():
    repo = RepositorioDeEstados()

    estado0 = EstadoCuantico("q0", [1.0, 0.0])
    estado1 = EstadoCuantico("q1", [0.0, 1.0])
    repo.agregar_estado(estado0)
    repo.agregar_estado(estado1)

    print("Estados iniciales:")
    for eid in repo.listar_estados():
        print(f" - {eid}: {repo.obtener_estado(eid).vector}")

    operador_X = OperadorCuantico("X", [[0, 1], [1, 0]])
    repo.aplicar_operador("q0", operador_X, nuevo_id="q0_X")

    print("\nEstados después de aplicar X a q0:")
    for eid in repo.listar_estados():
        print(f" - {eid}: {repo.obtener_estado(eid).vector}")

    repo.guardar("estados_guardados.json")
    print("\nEstados guardados.")
