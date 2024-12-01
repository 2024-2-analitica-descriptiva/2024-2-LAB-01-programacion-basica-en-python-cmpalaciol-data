"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    suma_por_letra = {}

    # Leer el archivo
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas
            columnas = line.strip().split('\t')
            # Extraer la letra de la columna 1 y los pares clave:valor de la columna 5
            letra = columnas[0]
            valores_columna_5 = columnas[4].split(',')

            # Sumar los valores de la columna 5
            suma_valores = sum(int(valor.split(':')[1]) for valor in valores_columna_5)

            # Actualizar la suma en el diccionario
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + suma_valores

    return suma_por_letra

# Llamada a la función para probar
print(pregunta_12())
