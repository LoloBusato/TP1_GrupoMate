from datos import obtener_lista_definiciones

def obtener_definiciones():
    # Hecha por Vicini Luciano
    """
    * funcion obtener_definiciones - importa el diccionario en formato lista, lo filtra y lo procesa
    *
    * pre: datos es un archivo con el diccionario en formato [palabra, definicion]
    *
    * post: devuelve el diccionario en formato
    *       {
    *           letra: [
    *               [palabra, definicion],
    *               ...
    *           ]
    *           ...
    *       }
    """
    # Constantes
    LETRAS_TILDADAS = {
        "á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u"
        }
    PALABRA = 0
    DEFINICION = 1
    INICIAL = 0
    LONG_MINIMA = 5

    cant_palabras_por_letra = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"ñ":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    cant_definiciones = 0
    definiciones = {}

    for definicion in obtener_lista_definiciones():
        if len(definicion[PALABRA]) >= LONG_MINIMA:
            letra = definicion[PALABRA][INICIAL]
            if definicion[PALABRA][INICIAL] in LETRAS_TILDADAS:
                letra = LETRAS_TILDADAS[letra]
            if letra in definiciones:
                definiciones[letra].append([definicion[PALABRA], definicion[DEFINICION]])
            else:
                definiciones[letra] = [[definicion[PALABRA], definicion[DEFINICION]]]
            cant_definiciones += 1
            cant_palabras_por_letra[letra] += 1        
    return definiciones
