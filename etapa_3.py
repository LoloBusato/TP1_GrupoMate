
def palabras_del_rosco (diccionario,letras):
    letras_tildadas = {"á":"a","é":"e","í":"i","ó":"o","ú":"u"}
    definiciones_rosco= []
    INICIAL = 0
    def chequeo_tilde(letra):
        if letra in letras_tildadas.keys():
            letra=letras_tildadas[letra]
        return letra
    '''
    recibe diccionario con formato {palabra: definicion} y listado de 10 letras participantes
    '''    
    palabras_lista = list(diccionario.keys())
    for letra in letras:
        indice = 0
        encontrado = False
        while indice < len(palabras_lista) and not encontrado:
            if palabras_lista[indice][INICIAL] == chequeo_tilde(letra):
                encontrado = True
                definiciones_rosco.append(palabras_lista[indice])
            indice += 1
    
    return sorted(definiciones_rosco)
