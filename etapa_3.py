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
    # Constantes
    PRIMERA_PALABRA_DEFINICION = 0

    definiciones_rosco = []
    
    for letra in letras:
        definiciones_rosco.append(diccionario[letra][PRIMERA_PALABRA_DEFINICION])

    return definiciones_rosco