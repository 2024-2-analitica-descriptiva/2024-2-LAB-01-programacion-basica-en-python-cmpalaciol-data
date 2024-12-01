"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    
    # Diccionario para almacenar los valores de la segunda columna por letra
    valores_por_letra = {}

    # Leer el archivo
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas
            columnas = line.split('\t')
            # Obtener la letra de la primera columna y el valor de la segunda columna
            letra = columnas[0]
            valor = int(columnas[1])

            # Actualizar los valores máximo y mínimo en el diccionario
            if letra not in valores_por_letra:
                valores_por_letra[letra] = [valor, valor]  # [maximo, minimo]
            else:
                valores_por_letra[letra][0] = max(valores_por_letra[letra][0], valor)
                valores_por_letra[letra][1] = min(valores_por_letra[letra][1], valor)

    # Convertir el diccionario en una lista de tuplas (letra, máximo, mínimo)
    resultado = [(letra, valores[0], valores[1]) for letra, valores in sorted(valores_por_letra.items())]

    return resultado

# Llamada a la función para probar
print(pregunta_05())

