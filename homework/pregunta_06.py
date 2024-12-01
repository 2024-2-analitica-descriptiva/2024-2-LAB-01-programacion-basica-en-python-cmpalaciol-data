"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
  
    # Diccionario para almacenar los valores mínimo y máximo por clave
    valores_por_clave = {}

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
                clave, valor = par.split(':')
                valor = int(valor)

                # Actualizar el mínimo y máximo para la clave en el diccionario
                if clave not in valores_por_clave:
                    valores_por_clave[clave] = [valor, valor]  # [minimo, maximo]
                else:
                    valores_por_clave[clave][0] = min(valores_por_clave[clave][0], valor)
                    valores_por_clave[clave][1] = max(valores_por_clave[clave][1], valor)

    # Convertir el diccionario en una lista de tuplas ordenada por clave
    resultado = [(clave, valores[0], valores[1]) for clave, valores in sorted(valores_por_clave.items())]

    return resultado

# Llamada a la función para probar
print(pregunta_06())

