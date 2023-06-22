import csv

NOMBRE = 0
VALOR = 1
def obtener_constantes():
    constantes = {}
    with open('configuracion.csv', 'r') as archivo:
        configuracion = csv.reader(archivo)
        for fila in configuracion:
            variable = fila[NOMBRE]
            valor = fila[VALOR]
            constantes[variable] = valor

    return constantes
    