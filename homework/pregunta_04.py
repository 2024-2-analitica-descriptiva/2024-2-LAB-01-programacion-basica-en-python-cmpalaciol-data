"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
# Diccionario para contar los registros por mes
    conteo_por_mes = {}

    # Leer el archivo
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas
            columnas = line.split('\t')
            # Extraer la fecha de la tercera columna
            fecha = columnas[2]
            # Extraer el mes de la fecha (posición 5 y 6 de la cadena)
            mes = fecha[5:7]
            # Incrementar el conteo del mes en el diccionario
            conteo_por_mes[mes] = conteo_por_mes.get(mes, 0) + 1

    # Convertir el diccionario en una lista de tuplas ordenada por el mes
    resultado = sorted(conteo_por_mes.items())

    return resultado

# Llamada a la función para probar
print(pregunta_04())