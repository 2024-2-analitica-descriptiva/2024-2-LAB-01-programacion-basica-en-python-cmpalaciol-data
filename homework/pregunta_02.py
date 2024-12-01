"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
# Diccionario para almacenar el conteo de letras
    conteo = {}

    # Leer el archivo
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Obtener la letra de la primera columna (índice 0)
            letra = line.split('\t')[0]
            # Incrementar el conteo en el diccionario
            conteo[letra] = conteo.get(letra, 0) + 1

    # Convertir el diccionario en una lista de tuplas ordenada alfabéticamente
    resultado = sorted(conteo.items())

    return resultado

# Llamada a la función para probar
print(pregunta_02())