from etapa_2 import definiciones
import random

letras_rosco= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
random.shuffle(letras_rosco)

definiciones_rosco= []

INICIAL = 0

def palabras_del_rosco (diccionario,letras):
    palabras_lista = list(diccionario.keys())
    for letra in letras:
        indice = 0
        encontrado = False
        while indice < len(palabras_lista) and not encontrado:
            if palabras_lista[indice][INICIAL] == letra:
                encontrado = True
                definiciones_rosco.append(palabras_lista[indice])
            indice += 1
    
    return sorted(definiciones_rosco)


