usuarios = {}

print("Hola, vamos a asignar tareas a los usuarios ")

def asignarTa(usuario, tarea):
    if usuario not in usuarios:
        usuarios[usuario] = []  
    informacionTa = {"tarea": tarea, "estado": "pendiente"}
    usuarios[usuario].append(informacionTa)
    print(f"Tarea '{tarea}' asignada a {usuario}.\n")

def actualizarTa(usuario, tarea, actualizar):
    if usuario in usuarios:
        tareasUsu = [t["tarea"] for t in usuarios[usuario]]
        
        if tarea not in tareasUsu:
            print(f"La tarea '{tarea}' no existe para el usuario {usuario}")
            return
        
        for t in usuarios[usuario]:
            if t["tarea"] == tarea:
                t["estado"] = actualizar
                print(f"Tarea '{tarea}' de {usuario} marcada como {actualizar}\n")
                return
    else:
        print(f"El usuario {usuario} no tiene tareas asignadas.\n")

def listarTa(usuario):
    if usuario in usuarios:
        print(f"Tareas de {usuario}:")
        for t in usuarios[usuario]:
            print(f"- {t['tarea']} [Estado: {t['estado']}]")
        print("")  
    else:
        print(f"El usuario {usuario} no tiene tareas asignadas.\n")

def tareas():
    while True:
        print("Menú:")
        print("1. Asignar tarea a un usuario")
        print("2. Actualizar estado de tarea")
        print("3. Listar tareas de un usuario")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            usuario = input("Ingresa el nombre del usuario: ")
            tarea = input("Ingresa la tarea a asignar: ")
            asignarTa(usuario, tarea)
        
        elif opcion == "2":
            usuario = input("Ingresa el nombre del usuario: ")
            listarTa(usuario)  
            if usuario in usuarios:
                tarea = input("Ingresa la tarea a actualizar: ")
                nuevo_estado = input("Ingresa el nuevo estado (completada/pendiente): ").lower()
                if nuevo_estado in ["completada", "pendiente"]:
                    actualizarTa(usuario, tarea, nuevo_estado)
                else:
                    print("Estado no válido. Debe ser 'completada' o 'pendiente'.\n")
            else:
                print(f"El usuario {usuario} no tiene tareas asignadas.\n")
        
        elif opcion == "3":
            usuario = input("Ingresa el nombre del usuario para listar sus tareas: ")
            listarTa(usuario)
        
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.\n")


tareas()
