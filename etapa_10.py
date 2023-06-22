import csv

#CONSTANTES========================================================================================================
NOMBRE = 0
VALOR = 1

#FUNCION========================================================================================================
def obtener_constantes():
    # Hecha por Busato Lorenzo
    """
    * funcion obtener_constantes  - lee el archivo configuracion.csv y crea un diccionario de constantes
    *
    * pre: configuracion.csv es un archivo con formato NOMBRE, VALOR por linea
    *
    * post: devuelve el diccionario en formato
    *       {
    *           NOMBRE: VALOR,
    *           ...
    *       }
    """
    constantes = {}
    with open('configuracion.csv', 'r') as archivo:
        configuracion = csv.reader(archivo)
        for linea in configuracion:
            variable = linea[NOMBRE]
            valor = linea[VALOR]
            constantes[variable] = valor

    return constantes
    