"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    suma_por_letra = {}

    # Leer el archivo
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas
            columnas = line.split('\t')
            # Obtener la letra de la primera columna y el valor de la segunda columna
            letra = columnas[0]
            valor = int(columnas[1])
            # Sumar el valor en el diccionario
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor

    # Convertir el diccionario en una lista de tuplas ordenada alfabéticamente
    resultado = sorted(suma_por_letra.items())

    return resultado

# Llamada a la función para probar
print(pregunta_03())
