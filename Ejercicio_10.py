
from modulo import funciones

names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA, CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia, Francsica, FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0,
11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2,
3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1,
0]

nombres = names.split(',')

estructura = funciones.generarEstructura(nombres, goals, goals_avoided, assists)

##print (estructura)

funciones.imprimirGoleadxr(estructura)

puntajes = {nombre: funciones.calcular_puntaje(datos) for nombre, datos in estructura.items()}
jugador_mas_influyente = max(puntajes, key=puntajes.get)

print("El jugador mas influyente es: ",jugador_mas_influyente," con un puntaje de", puntajes[jugador_mas_influyente])


total_goles = sum(goals)


print("El promedio de goles por partido del equipo en general es:", funciones.calcular_promedio(total_goles))

funciones.promedio_goles_goleador(estructura)
