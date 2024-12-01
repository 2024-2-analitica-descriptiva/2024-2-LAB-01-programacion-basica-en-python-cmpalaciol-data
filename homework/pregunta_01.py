"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    
    """
    Retorne la suma de la segunda columna del archivo data.csv.
    """
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()
    
    # Extraer la segunda columna (índice 1)
    suma = sum(int(line.split('\t')[1]) for line in lines)
    
    return suma

# Llamada a la función para probar
print(pregunta_01())
