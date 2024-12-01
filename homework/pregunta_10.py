"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
   
    # Lista para almacenar las tuplas resultantes
    resultado = []

    # Leer el archivo
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas
            columnas = line.strip().split('\t')
            # Extraer los datos necesarios
            letra = columnas[0]  # Columna 1
            elementos_columna_4 = len(columnas[3].split(','))  # Cantidad de elementos en columna 4
            elementos_columna_5 = len(columnas[4].split(','))  # Cantidad de elementos en columna 5
            # Crear una tupla y agregarla al resultado
            resultado.append((letra, elementos_columna_4, elementos_columna_5))

    return resultado

# Llamada a la función para probar
print(pregunta_10())

