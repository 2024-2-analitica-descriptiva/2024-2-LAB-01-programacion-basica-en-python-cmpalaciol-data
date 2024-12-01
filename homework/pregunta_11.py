"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
   
    # Diccionario para almacenar la suma por letra
    suma_por_letra = {}

    # Leer el archivo
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas
            columnas = line.strip().split('\t')
            # Extraer el valor de la columna 2 y las letras de la columna 4
            valor_columna_2 = int(columnas[1])
            letras_columna_4 = columnas[3].split(',')

            # Sumar el valor de la columna 2 para cada letra en la columna 4
            for letra in letras_columna_4:
                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor_columna_2

    # Retornar el diccionario ordenado alfabéticamente por clave
    return dict(sorted(suma_por_letra.items()))

# Llamada a la función para probar
print(pregunta_11())

