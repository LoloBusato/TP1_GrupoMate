from datos import obtener_lista_definiciones
letras_tildadas= {"á":"a","é":"e","í":"i","ó":"o","ú":"u"}
cant_palabras_por_letra= {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"ñ":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
definiciones= {}
cant_definiciones= 0
PALABRA = 0
DEFINICION = 1
INICIAL = 0

for definicion in obtener_lista_definiciones():
    if len(definicion[PALABRA]) >= 5:
        definiciones[definicion[PALABRA]] = definicion[DEFINICION]
        letra= definicion[PALABRA][INICIAL]
        if letra in letras_tildadas.keys():
            letra= letras_tildadas[letra]
        cant_definiciones += 1
        cant_palabras_por_letra[letra] += 1
        
print (f'la cantidad de palabras por letra son:\n{cant_palabras_por_letra}')
print (f'la cantidad total de definiciones son: {cant_definiciones}')
