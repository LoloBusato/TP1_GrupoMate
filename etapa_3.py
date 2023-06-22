import random

def palabras_del_rosco(diccionario,letras):
    # Hecha por Vicini Luciano
    """
        * funcion palabras_del_rosco - recibe diccionario y listado de 10 letras participantes
        *           Selecciona una palabra de cada letra del diccionario
        *
        * pre: diccionario es un diccionario con formato valido, letras es una lista de letras ordenadas
        *
        * post: devuelve una lista ordenada con las palabras y definiciones seleccionadas
    """
    definiciones_rosco = []

    for letra in letras:
        cantidad_palabras = (len(diccionario[letra]) - 1)
        indice_palabra_random = random.randint(0, cantidad_palabras)
        definiciones_rosco.append(diccionario[letra][indice_palabra_random])

    return definiciones_rosco