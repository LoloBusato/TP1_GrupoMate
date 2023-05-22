import random
from etapa_2 import obtener_definiciones
from etapa_3 import palabras_del_rosco
import doctest
# Constantes =======================================================================================================================
PUNTAJE_ACIERTO = 10
PUNTAJE_ERROR = 3
CANTIDAD_LETRAS_ROSCO = 10
INICIAL = 0
LETRAS_TILDADAS = {
    'á':'a',
    'é':'e',
    'í':'i',
    'ó':'o',
    'ú':'u'
}
# Funciones =======================================================================================================================
def letras_participantes():
    '''
    * Mezcla las letras del abecedario y selecciona las primeras diez del listado como letras participantes del juego
        
    * Post: Devuelve una lista con 10 valores (CANTIDAD_LETRAS_ROSCO), cada uno una letra distinta
    '''
    letras_rosco= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    random.shuffle(letras_rosco)
    return sorted(letras_rosco[:CANTIDAD_LETRAS_ROSCO])

def formateo_resultados(resultados):
    '''
    * Función que da formato de impresión al listado de resultados
    
    * Pre: resultados es una lista con valores posibles 'a' en caso de acierto, 'e' en caso de error y ' 'en caso de que no se haya evaluado aún esa respuesta
    
    * Post: Devuelve un formato de impresión con los mismos valores recibidos
    '''
    resultados_a_imprimir = ""
    for letra in resultados:
        if letra:
            resultados_a_imprimir +=f"[{letra}]"
        else:
            resultados_a_imprimir +=f"[ ]"
    return resultados_a_imprimir
def imprimir_resultados(abecedario_imprimir, resultados, aciertos, errores, palabra, definicion):
    """
    * Función que se encarga de la impresión de cada partida del juego y se acciona luego de cada intento 
    
    * Pre: Recibe las letras participantes, los resultados parciales, la cantidad de aciertos y errores, la palabra del turno y su definición
    
    * Post: Imprime el tablero de letras, los resultados parciales, la palabra de turno y su definición
    """
    print(abecedario_imprimir)
    resultado_imprimir = formateo_resultados(resultados)
    print(resultado_imprimir + "\n\n")
    
    print(f"Aciertos: {aciertos}")
    print(f"Errores: {errores}")
    
    print(f"Turno letra {palabra[0].upper()} - Palabra de {len(palabra)} letras")

    print(f"Definición: {definicion}")

def pedir_palabra():
    '''
    * Función que se encarga de pedir al jugador una respuesta para la palabra de turno
    '''
    respuesta = input("Ingrese palabra: ")
    while not respuesta.isalpha():
        print("Respuesta inválida, intente nuevamente")
        respuesta = input("Ingrese palabra: ")
    return respuesta
def reemplaza_tildes(palabra):
    '''
    * Función que reemplaza los tildes de las palabras, de encontrar alguna
    
    * Pre: Recibe una cadena
    
    * Post: Devuelve la misma palabra sin tildes
    *
    >>> reemplaza_tildes('esdrújula')
    'esdrujula'
    >>> reemplaza_tildes('canción')
    'cancion'
    >>> reemplaza_tildes('magia')
    'magia'
    '''
    palabra_en_lista = list(palabra)
    indice = 0
    tilde_encontrada = False
    while (indice < len(palabra_en_lista) and not tilde_encontrada):
        if palabra_en_lista[indice] in LETRAS_TILDADAS.keys():
            palabra_en_lista[indice] = LETRAS_TILDADAS[palabra_en_lista[indice]]
            tilde_encontrada = True
        indice +=1
    palabra_procesada = ''.join(palabra_en_lista)
    return palabra_procesada
def valida_respuesta(palabra_usuario,palabra):
    '''
    * Función que evalúa si la palabra otorgada es correcta o no
    
    * Pre: Recibe la palabra ingresada por input por el usuario y la palabra a adivinar 
    
    * Post: Retorna True o False segun la respuesta sea correcta o no
    >>> valida_respuesta('cancion','canción')
    True
    >>> valida_respuesta('perrito','perito')
    False
    >>> valida_respuesta('teclado','teclado')
    True
    >>> valida_respuesta('pérro','perro')
    False
    '''
    palabra = reemplaza_tildes(palabra)
    respuesta = palabra_usuario.lower() == palabra.lower()
    return respuesta

def impresion_final(puntaje, resumen_partida):
    '''
    * Función que imprime el puntaje final de cada partida
    
    * Pre: recibe los puntajes finales como un número entero y el resumen de partida, como una cadena formateada con cada respuesta correcta, su definición y la respuesta otorgada por el usuario
    
    * Post: imprime los resultados
    '''
    print(resumen_partida)
    print(f"Puntaje final: {puntaje}")

# Cuerpo =======================================================================================================================
def partida_pasapalabra(puntaje = 0):
    '''
    * Función que ejecuta cada partida de pasapalabra
    
    * Pre: recibe o inicializa en 0, según corresponda, el puntaje de la partida global
    
    * Post: Ejecuta la partida hasta que se recorra la totalidad de la lista de letras, con una respuesta válida por cada letra participante
    '''
    #1. Se deberá comenzar con la generación del diccionario de palabras.
    definiciones = obtener_definiciones()
    #2. Luego se deben seleccionar las 10 letras participantes.
    LETRAS= letras_participantes()
    #3. El programa elegirá al azar la lista de palabras a adivinar por el jugador.
    palabras_seleccionadas= palabras_del_rosco(definiciones, LETRAS)
    #4. Luego se armará el tablero que visualizará el usuario, y dará comienzo la partida

    def palabras(indice):
        '''
        * Selecciona cada palabra de la lista de palabras seleccionadas, segun corresponda, y la retorna
        
        * Pre: recibe el índice correspondiente a la palabra de turno
        
        * Post: retorna la palabra de turno
        '''
        palabra= palabras_seleccionadas[indice]
        return palabra

    def funcion_definiciones (indice):
        '''
        * Selecciona cada definición de la lista de definiciones, segun corresponda, y la retorna
        
        * Pre: recibe el índice correspondiente a la definición de turno
        
        * Post: retorna la definición de turno
        '''
        palabra= palabras_seleccionadas[indice]
        definicion= definiciones[palabra]
        return definicion


    # Se crean las variables abecedario y se les da formato a las mismas
    resultados = []
    abecedario_imprimir = ""
    for letra in LETRAS:
        abecedario_imprimir += f"[{letra.upper()}]"
        resultados.append(" ")
    
    # Se definen las variables que contabilizan los aciertos, los errores, la posición del rosco en la que se encuentra y el resumen final
    aciertos = 0
    errores = 0
    indice = 0                
    resumen_partida = ""

    #Se da inicio al ciclo que engloba el rosco. Finaliza al resolver todas las palabras
    while indice < len(LETRAS):

        imprimir_resultados(abecedario_imprimir, resultados, aciertos, errores, palabras(indice), funcion_definiciones(indice))
        palabra_usuario = pedir_palabra()
        respuesta = valida_respuesta(palabra_usuario,palabras(indice))
        if respuesta:
            resumen_partida += (f"\nTurno letra {palabras(indice)[INICIAL].upper()} - Palabra de {len(palabras(indice))} letras - {palabra_usuario} - acierto")
            print("Palabra correcta")
            aciertos +=1
            resultados[indice]="a"
            puntaje += PUNTAJE_ACIERTO
            indice +=1
        else:
            resumen_partida += (f"\nTurno letra {palabras(indice)[INICIAL].upper()} - Palabra de {len(palabras(indice))} letras - {palabra_usuario} - error - Palabra Correcta: {palabras(indice)}")
            print (f"Palabra incorrecta - Respuesta: {palabras(indice)}")
            errores +=1
            resultados[indice]= "e"
            puntaje -= PUNTAJE_ERROR
            indice+=1

    impresion_final(puntaje, resumen_partida)
    return puntaje
print(doctest.testmod())







