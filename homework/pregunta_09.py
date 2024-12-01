"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    # Diccionario para almacenar el conteo de registros por clave
    conteo_por_clave = {}

    # Leer el archivo
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas
            columnas = line.split('\t')
            # Extraer la columna 5
            columna_5 = columnas[4]
            # Dividir la columna 5 en pares clave:valor
            pares = columna_5.strip().split(',')

            for par in pares:
                # Separar clave y valor
                clave, _ = par.split(':')
                # Incrementar el conteo de la clave en el diccionario
                conteo_por_clave[clave] = conteo_por_clave.get(clave, 0) + 1

    return conteo_por_clave

# Llamada a la función para probar
print(pregunta_09())
