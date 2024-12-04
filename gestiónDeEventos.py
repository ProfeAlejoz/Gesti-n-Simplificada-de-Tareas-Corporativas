nombre_evento = "Conferencia de Prensa"
fecha_evento = "2024-12-15"
aforo_maximo = 3
participantes = {}

def registrar(participante):
    if len(participantes) < aforo_maximo:
        participantes[participante] = True
        print(f"{participante} se ha registrado correctamente en {nombre_evento}.")
    else:
        print(f"No se puede registrar a {participante}. El evento está lleno.")

def cancelar(participante):
    if participante in participantes:
        del participantes[participante]
        print(f"{participante} ha sido eliminado de {nombre_evento}.")
    else:
        print(f"{participante} no estaba registrado en {nombre_evento}.")

def mostrar_info():
    print(f"\n--- Información del Evento ---")
    print(f"Evento: {nombre_evento}")
    print(f"Fecha: {fecha_evento}")
    print(f"Aforo máximo: {aforo_maximo}")
    print(f"Participantes: {', '.join(participantes.keys()) if participantes else 'Ninguno'}")
    print("------------------------------\n")

if __name__ == "__main__":
    mostrar_info()

    registrar("Juan")
    registrar("María")
    registrar("Carlos")
    registrar("Luis")

    mostrar_info()

    cancelar("María")
    cancelar("Ana")

    mostrar_info()
