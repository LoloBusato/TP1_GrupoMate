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
    *
    * Post: Devuelve una lista con 10 valores (CANTIDAD_LETRAS_ROSCO), cada uno una letra distinta
    '''
    LETRAS_ROSCO= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    random.shuffle(LETRAS_ROSCO)
    return sorted(LETRAS_ROSCO[:CANTIDAD_LETRAS_ROSCO])

def formateo_resultados(resultados):
    '''
    * Función que da formato de impresión al listado de resultados
    *
    * Pre: resultados es una lista con valores posibles 'a' en caso de acierto, 'e' en caso de error y ' 'en caso de que no se haya evaluado aún esa respuesta
    *
    * Post: Devuelve un formato de impresión con los mismos valores recibidos
    '''
    resultados_a_imprimir = ""
    for letra in resultados:
        if letra:
            resultados_a_imprimir += f"[{letra}]"
        else:
            resultados_a_imprimir += f"[ ]"
    return resultados_a_imprimir

def imprimir_resultados(abecedario_imprimir, resultados, aciertos, errores, palabra, definicion):
    """
    * Función que se encarga de la impresión de cada turno del juego y se acciona luego de cada intento 
    *
    * Pre: Recibe las letras participantes ordenadas, los resultados parciales, la cantidad de aciertos y errores, la palabra del turno y su definición
    *
    * Post: Imprime el tablero de letras, los resultados parciales, la palabra de turno y su definición
    
    >>> abecedario_imprimir = "[A][B][C][D]"
    >>> resultados=["a","e"," "," "]
    >>> aciertos = 1
    >>> errores = 1
    >>> palabra = "circuito"
    >>> definicion = "1.  m. Terreno comprendido dentro de un perímetro cualquiera"
    >>> imprimir_resultados(abecedario_imprimir, resultados, aciertos, errores, palabra, definicion)
    [A][B][C][D]
    [a][e][ ][ ]
    <BLANKLINE>
    <BLANKLINE>
    Aciertos: 1
    Errores: 1
    Turno letra C - Palabra de 8 letras
    Definición: 1.  m. Terreno comprendido dentro de un perímetro cualquiera
    """
    print(abecedario_imprimir)
    resultado_imprimir = formateo_resultados(resultados)
    print(resultado_imprimir + "\n\n")
    
    print(f"Aciertos: {aciertos}")
    print(f"Errores: {errores}")
    
    print(f"Turno letra {palabra[0].upper()} - Palabra de {len(palabra)} letras")

    print(f"Definición: {definicion}")

def pedir_palabra(longitud):
    '''
    * Función que se encarga de pedir al jugador una respuesta para 
    *       la palabra de turno y revisa si tiene el formato y tamanio pedido
    *
    * Pre: recibe "longitud" que es el tamanio de la palabra actual
    *
    * Post: si es valida devuelve la respuesta del usuario
    '''
    respuesta = input("Ingrese palabra: ")
    while not respuesta.isalpha() or len(respuesta) != longitud:
        print("Respuesta inválida, intente nuevamente")
        respuesta = input("Ingrese palabra: ")
    return respuesta

def reemplaza_tildes(palabra):
    '''
    * Función que reemplaza los tildes de las palabras, de encontrar alguna
    *
    * Pre: Recibe una cadena
    *
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

def valida_respuesta(palabra_usuario, palabra_actual):
    '''
    * Función que evalúa si la palabra otorgada es correcta o no
    
    * Pre: Recibe la palabra ingresada por input por el usuario y la palabra a adivinar 
    
    * Post: Retorna True o False segun la respuesta sea correcta o no
    >>> valida_respuesta('cancion','canción')
    True
    >>> valida_respuesta('perrito','peritos')
    False
    >>> valida_respuesta('teclado','teclado')
    True
    >>> valida_respuesta('pérro','perro')
    False
    '''
    palabra_actual = reemplaza_tildes(palabra_actual)
    respuesta = palabra_usuario.lower() == palabra_actual.lower()
    return respuesta

def impresion_final(puntaje, resumen_partida):
    '''
    * Función que imprime el puntaje final de cada partida
    *
    * Pre: recibe los puntajes finales como un número entero y el resumen de partida, como una cadena formateada
    *      con cada respuesta correcta, su definición y la respuesta otorgada por el usuario
    *
    * Post: imprime los resultados
    '''
    print(resumen_partida)
    print(f"Puntaje final: {puntaje}")

def iniciar_resultados_abecedario(letras):
    '''
    * Función que se encarga de iniciar las variables resultados y abecedario_imprimir
    *
    * Pre: recibe "letras" que es una lista ordenada con las letras participantes
    *
    * Post: devuelve resultados como una lista con cadenas de caracter vacias y
    *       devuelve abecedario_imprimir con las letras participantes para imprimir
    '''
    resultados = []
    abecedario_imprimir = ""
    for letra in letras:
        abecedario_imprimir += f"[{letra.upper()}]"
        resultados.append(" ")
    return resultados, abecedario_imprimir

# Cuerpo =======================================================================================================================
def partida_pasapalabra(puntaje = 0):
    '''
    * Función que ejecuta cada partida de pasapalabra
    *
    * Pre: recibe o inicializa en 0, según corresponda, el puntaje de la partida global
    *
    * Post: Ejecuta la partida hasta que se recorra la totalidad de la lista de letras, con una respuesta válida por cada letra participante
    '''
    #1. Se deberá comenzar con la generación del diccionario de palabras.
    DICCIONARIO = obtener_definiciones()
    #2. Luego se deben seleccionar las 10 letras participantes.
    LETRAS= letras_participantes()
    #3. El programa elegirá al azar la lista de palabras, definicion a adivinar por el jugador.
    DICCIONARIO_SELECCIONADO = palabras_del_rosco(DICCIONARIO, LETRAS)
    #4. Luego se armará el tablero que visualizará el usuario, y dará comienzo la partida

    PALABRA = 0
    DEFINICION = 1
    # Se crean las variables abecedario y se les da formato a las mismas
    resultados, abecedario_imprimir = iniciar_resultados_abecedario(LETRAS)
    
    # Se definen las variables que contabilizan los aciertos, los errores, la posición del rosco en la que se encuentra y el resumen final
    aciertos = 0
    errores = 0
    indice = 0                
    resumen_partida = ""

    #Se da inicio al ciclo que engloba el rosco. Finaliza al resolver todas las palabras
    while indice < len(LETRAS):
        palabra_actual = DICCIONARIO_SELECCIONADO[indice][PALABRA]
        definicion_actual = DICCIONARIO_SELECCIONADO[indice][DEFINICION]

        imprimir_resultados(abecedario_imprimir, resultados, aciertos, errores, palabra_actual, definicion_actual)

        palabra_usuario = pedir_palabra(len(palabra_actual))
        respuesta = valida_respuesta(palabra_usuario, palabra_actual)
        if respuesta:
            resumen_partida += (f"\nTurno letra {palabra_actual[INICIAL].upper()} - Palabra de {len(palabra_actual)} letras - {palabra_usuario} - acierto")
            print("Palabra correcta")
            aciertos += 1
            resultados[indice] = "a"
            puntaje += PUNTAJE_ACIERTO
            indice += 1
        else:
            resumen_partida += (f"\nTurno letra {palabra_actual[INICIAL].upper()} - Palabra de {len(palabra_actual)} letras - {palabra_usuario} - error - Palabra Correcta: {palabra_actual}")
            print (f"Palabra incorrecta - Respuesta: {palabra_actual}")
            errores +=1
            resultados[indice] = "e"
            puntaje -= PUNTAJE_ERROR
            indice += 1

    impresion_final(puntaje, resumen_partida)
    return puntaje

print(doctest.testmod())