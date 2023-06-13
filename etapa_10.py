import csv

def obtener_constantes():
    datos = {}
    with open('configuracion.csv', 'r') as archivo:
        reader = csv.reader(archivo)

        for fila in reader:
            variable = fila[0]
            valor = int(fila[1])
            datos[variable] = valor
    return datos
    