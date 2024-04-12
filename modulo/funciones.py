def generarEstructura(nombres, goals, goals_avoided, assists):
    # Crear un diccionario vacío para almacenar los datos
    jugadores = {}

    # Iterar sobre las listas y agregar los datos al diccionario
    for nombre, gol, gol_evitado, asistencia in zip(nombres, goals, goals_avoided, assists):
        # Limpiar el nombre eliminando comas y espacios adicionales
        nombre = nombre.strip(',').strip()
        # Agregar los datos al diccionario
        jugadores[nombre] = {'goles': gol, 'goles evitados': gol_evitado, 'asistencias': asistencia}

    # Retornar el diccionario
    return jugadores


def imprimirGoleadxr(estructura):
    # Identificar al jugador con más goles
    jugador_con_mas_goles = max(estructura, key=lambda x: estructura[x]['goles'])

    # Obtener la cantidad de goles del jugador con más goles
    goles_del_goleador_o_goleadora = estructura[jugador_con_mas_goles]['goles']

    print("El goleador o goleadora es:", jugador_con_mas_goles)
    print("Cantidad de goles:", goles_del_goleador_o_goleadora)



def calcular_puntaje (jugador):
    return (jugador['goles'] * 1.5) + (jugador['goles evitados'] * 1.25) + (jugador['asistencias'] * 1)

def calcular_promedio(total_goles):
    return total_goles / 25

def promedio_goles_goleador(estructura):
    # Identificar al jugador con más goles
    jugador_con_mas_goles = max(estructura, key=lambda x: estructura[x]['goles'])

    # Calcular el total de goles del jugador con más goles
    goles_del_goleador = estructura[jugador_con_mas_goles]['goles']

    # Calcular el promedio de goles por partido del goleador o goleadora
    promedio_goles_por_partido_goleador = goles_del_goleador / 25

    print("El promedio de goles por partido del goleador o goleadora es:", promedio_goles_por_partido_goleador)