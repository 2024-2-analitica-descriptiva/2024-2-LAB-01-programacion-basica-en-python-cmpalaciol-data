"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    # Diccionario para asociar los valores de la columna 2 con letras únicas
    asociacion = {}

    # Leer el archivo
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas
            columnas = line.split('\t')
            # Extraer la letra de la columna 1 y el valor de la columna 2
            letra = columnas[0]
            valor = int(columnas[1])

            # Actualizar el conjunto de letras asociadas al valor
            if valor not in asociacion:
                asociacion[valor] = set()
            asociacion[valor].add(letra)

    # Convertir los conjuntos a listas, ordenarlas y crear una lista de tuplas
    resultado = [(valor, sorted(list(letras))) for valor, letras in sorted(asociacion.items())]

    return resultado

# Llamada a la función para probar
print(pregunta_08())

