usuarios = [
    {"id": 1, "nombre": "alex", "tareas": [1, 2], "eventos": [1]},
    {"id": 2, "nombre": "Pepe", "tareas": [2, 3], "eventos": [1, 2]},
    {"id": 3, "nombre": "Carlos", "tareas": [1], "eventos": []},
]
tareas = [
    {"id": 1, "descripcion": "Tarea 1", "completada": True},
    {"id": 2, "descripcion": "Tarea 2", "completada": False},
    {"id": 3, "descripcion": "Tarea 3", "completada": True},
]
eventos = [
    {"id": 1, "nombre": "Evento 1"},
    {"id": 2, "nombre": "Evento 2"},
]
def contarElementos(usuarios, tareas, eventos):
    toUsers = len(usuarios)
    toTareas = len(tareas)
    toEvents = len(eventos)
    return toUsers, toTareas, toEvents
def resumenEstadisticas(tareas):
    total_tareas = len(tareas)
    if total_tareas == 0:
        porcentajeCompletadas = 0
    else:
        tareasCompletadas = sum(1 for tarea in tareas if tarea["completada"])
        porcentajeCompletadas = (tareasCompletadas / toTareas) * 100
    return porcentajeCompletadas

def eventosPorUsuario(usuarios):
    eventosInscritos = {}
    for usuario in usuarios:
        eventosInscritos[usuario["nombre"]] = len(usuario["eventos"])
    return eventosInscritos

toUsers, toTareas, toEvents = contarElementos(usuarios, tareas, eventos)
porcentajeCompletadas = resumenEstadisticas(tareas)
eventosInscritos = eventosPorUsuario(usuarios)


print(f"Número total de usuarios: {toUsers}\n-----------------------------")
print(f"Número total de tareas: {toTareas}\n-----------------------------")
print(f"Número total de eventos: {toEvents}\n-----------------------------")
print(f"Porcentaje de tareas completadas: {porcentajeCompletadas:.2f}%\n-----------------------------")
print("Cantidad de eventos en los que cada usuario está inscrito:\n-----------------------------")
for usuario, cantidad in eventosInscritos.items():
    print(f"{usuario}: {cantidad} evento(s)\n^^^^^^^^^^^^^^^^^^^^")