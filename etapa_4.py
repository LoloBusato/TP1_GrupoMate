import random
import doctest
from etapa_10 import obtener_constantes

# Constantes =======================================================================================================================
CONFIGURACION = obtener_constantes()
LETRAS_TILDADAS = {
    'á':'a',
    'é':'e',
    'í':'i',
    'ó':'o',
    'ú':'u'
}
# Funciones =======================================================================================================================

def formateo_resultados(resultados):
    # Hecha por Orlando Martín
    """
    * Función que da formato de impresión al listado de resultados
    *
    * Pre: resultados es una lista con valores posibles 'a' en caso de acierto, 
    *   'e' en caso de error y ' 'en caso de que no se haya evaluado aún esa respuesta
    *
    * Post: Devuelve un formato de impresión con los mismos valores recibidos
    *
    >>> formateo_resultados(['a','e'])
    '[a][e]'
    >>> formateo_resultados(['e','e','a','a',' ',' '])
    '[e][e][a][a][ ][ ]'
    >>> formateo_resultados([' ',' ',' '])
    '[ ][ ][ ]'
    """
    resultados_a_imprimir = ""
    for letra in resultados:
        if letra:
            resultados_a_imprimir += f"[{letra}]"
        else:
            resultados_a_imprimir += f"[ ]"
    return resultados_a_imprimir

def reemplaza_tildes(palabra):
    # Hecha por Orlando Martín
    """
    * Función que reemplaza los tildes de las palabras, de encontrar alguna
    *
    * Pre: Recibe una cadena de caracteres
    *
    * Post: Devuelve la misma palabra sin tildes
    *
    >>> reemplaza_tildes('esdrújula')
    'esdrujula'
    >>> reemplaza_tildes('magia')
    'magia'
    """
    palabra_en_lista = list(palabra)
    indice = 0
    tilde_encontrada = False
    while (indice < len(palabra_en_lista) and not tilde_encontrada):
        if palabra_en_lista[indice] in LETRAS_TILDADAS.keys():
            palabra_en_lista[indice] = LETRAS_TILDADAS[palabra_en_lista[indice]]
            tilde_encontrada = True
        indice += 1
    palabra_procesada = ''.join(palabra_en_lista)
    return palabra_procesada

def valida_respuesta(palabra_usuario, palabra_actual):
    # Hecha por Orlando Martín
    """
    * Función que evalúa si la palabra del usuario es correcta o no
    
    * Pre: Recibe la palabra ingresada por el usuario y la palabra a adivinar 
    
    * Post: Retorna True o False segun la respuesta sea correcta o no
    >>> valida_respuesta('cancion','canción')
    True
    >>> valida_respuesta('perrito','peritos')
    False
    >>> valida_respuesta('pérro','perro')
    False
    """
    palabra_actual = reemplaza_tildes(palabra_actual)
    return palabra_usuario.lower() == palabra_actual.lower()


def iniciar_resultados_abecedario(letras,resultados,jugadores):
    # Hecha por Orlando Martín
    """
    * Función que se encarga de iniciar las variables resultados y abecedario_imprimir
    *
    * Pre: recibe "letras" que es una lista ordenada con las letras participantes y 
    *   "resultados" que es una lista ordenada con los aciertos o errores de cada letra
    *   "jugadores" que es una lista ordenada con los intentos de cada jugador
    * Post: devuelve "resultados" como una lista con cadenas de caracter vacias, "abecedario_imprimir" con las letras participantes para imprimir y "jugadores" con el listado de participaciones para imprimir
    *
    >>> iniciar_resultados_abecedario(["a","b","c","d"],[' ',' ',' ',' '],[' ',' ',' ',' '])
    ([' ', ' ', ' ', ' '], '[A][B][C][D]', [' ', ' ', ' ', ' '])
    >>> iniciar_resultados_abecedario(["A","f","h","r"],['a','e',' ',' '],[1,1,' ',' '])
    (['a', 'e', ' ', ' '], '[A][F][H][R]', [1, 1, ' ', ' '])
    """
    abecedario_imprimir = ""
    indice = 0
    for letra in letras:
        abecedario_imprimir += f"[{letra.upper()}]"
        if not resultados[indice]:
            resultados[indice] = " "
        if not jugadores[indice]:
            jugadores[indice] = " "
    return resultados, abecedario_imprimir, jugadores

def imprimir_resultados(abecedario_imprimir, resultados, palabra, definicion, partida, jugadores, jugador, jugadores_imprimir, indice_jugador):
    # Hecha por Busato Lorenzo
    """
    * Función que se encarga de la impresión de cada turno del juego y se acciona luego de 
    *   cada intento 
    *
    * Pre: Recibe las letras participantes ordenadas, los resultados parciales, la palabra 
    *   del turno, su definición, el diccionario de partida, el listado de jugadores, el nombre del jugador participante, el listado ordenado de participaciones del rosco y el indice del jugador *    actual
    *
    * Post: Imprime el tablero de letras, los resultados parciales, la palabra de turno 
    *   y su definición
    * 
    >>> abecedario_imprimir = "[A][B][C][D][E][F][G]"
    >>> resultados=["a","a","e","a","e","a",' ']
    >>> palabra = "circuito"
    >>> definicion = "def de circuito"
    >>> partida = {'jugador':[1,1,1,2,2,1,' '],'resultados':['a','a','e','a','e','a',' ']}
    >>> jugadores = ['martin','lorenzo']
    >>> jugadores_imprimir=[1,1,1,2,2,1,' ']
    >>> jugador = 'martin'
    >>> numero_jugador=1
    >>> imprimir_resultados(abecedario_imprimir, resultados, palabra, definicion,partida, jugadores,jugador,jugadores_imprimir,numero_jugador)
    [A][B][C][D][E][F][G]
    [1][1][1][2][2][1][ ]
    [a][a][e][a][e][a][ ]
    <BLANKLINE>
    <BLANKLINE>
    Jugadores:
    1. martin - Aciertos: 3 - Errores : 1
    2. lorenzo - Aciertos: 1 - Errores : 1
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    Turno  Jugador 1 martin - letra C - Palabra de 8 letras
    Definición: def de circuito
    """
    print(abecedario_imprimir)
    jugadores_imprimir = formateo_resultados(jugadores_imprimir)
    resultado_imprimir = formateo_resultados(resultados)
    print(jugadores_imprimir)
    print(resultado_imprimir + "\n\n")
    
    print('Jugadores:')
    imprimir_resultados_parciales(partida,jugadores)
    print("\n\n")
        
    print(f"Turno  Jugador {indice_jugador} {jugador} - letra {palabra[int(CONFIGURACION['INICIAL'])].upper()} - Palabra de {len(palabra)} letras")

    print(f"Definición: {definicion}")

def pedir_palabra(longitud):
    # Hecha por Busato Lorenzo
    """
    * Función que se encarga de pedir al jugador una respuesta para 
    *       la palabra de turno y revisa si tiene el formato y tamanio pedido
    *
    * Pre: recibe "longitud" que es el tamanio de la palabra actual
    *
    * Post: si es valida devuelve la respuesta del usuario y sino vuelve a pedir una respuesta
    """
    respuesta = input("Ingrese palabra: ")
    while not respuesta.isalpha() or len(respuesta) != longitud:
        print("Respuesta inválida, intente nuevamente")
        respuesta = input("Ingrese palabra: ")
    return respuesta

def impresion_final(puntaje, resumen_partida):
    # Hecha por Busato Lorenzo
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

def letras_participantes():
    # Hecho por Nuñez Juan Bautista
    '''
    * Mezcla las letras del abecedario y selecciona las primeras diez del listado como letras participantes del juego
    *
    * Post: Devuelve una lista con 10 valores (CANTIDAD_LETRAS_ROSCO), cada uno una letra distinta
    '''
    LETRAS_ROSCO = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    random.shuffle(LETRAS_ROSCO)
    return sorted(LETRAS_ROSCO[:int(CONFIGURACION['CANTIDAD_LETRAS_ROSCO'])])

def selecciona_jugador(indice,jugadores):
    # Hecha por Orlando Martin
    """
    * Función que selecciona un jugador de un listado dependiendo de su índice
    *
    * Pre: Recibe un número indice y un listado con todos los jugadores participantes 
    *   de la partida
    * 
    * Post: Retorna el nombre del jugador correspondiente. Si no coresponde seleccionar 
    *   un jugador, retorna un string vacio
    *
    >>> indice = 3
    >>> jugadores = ['martin','lorenzo','luciano','juan']
    >>> selecciona_jugador(indice,jugadores)
    'juan'
    >>> indice_2 = -1
    >>> selecciona_jugador(indice_2,jugadores)
    ''
    """
    return '' if indice == -1 else jugadores[indice]

def incrementa_jugador(cantidad_jugadores,indice=-1):
    # Hecha por Orlando Martin
    """
    * Función encargada de incrementar el indice de los jugadores reiniciando el valor una vez 
    *   que se llegue al final del listado
    * 
    * Pre: Recibe un numero indicador de la cantidad de jugadores participantes y el índice 
    *   actual, siendo -1 el valor por defecto en caso de que no se ingrese como parametro
    * 
    * Post: Devuelve un número índice incrementado en uno
    >>> incrementa_jugador(3)
    0
    >>> incrementa_jugador(3,2)
    0
    >>> incrementa_jugador(3,1)
    2
    """
    indice += 1
    return 0 if indice == cantidad_jugadores else indice


def contador_aciertos(resultados, numero, jugadores_turno):
    # Hecha por Orlando Martin
    """
    * Función encargada de contar los aciertos y errores de cada jugador
    *
    * Pre: Recibe el listado reusltados, con una lista de aciertos o errores, numero es un *numero de indicie del jugador y jugadores_turno un listado con las respuestas correspondientes de cada * usuario
    * 
    * Post: Retorna una tupla con la cantidad de aciertos y errores del usuario
    *
    >>> contador_aciertos(['a','a','e','a',' '],1,[1,1,1,2,' '])
    (2, 1)
    >>> contador_aciertos(['a','a','e','a'],2,[1,1,1,2,' '])
    (1, 0)
    >>> contador_aciertos(['a','a','a'],2,[1,1,1])
    (0, 0)
    """
    aciertos = 0
    errores = 0
    indice = 0
    for respuesta in resultados:
        if(jugadores_turno[indice] == numero):
            if respuesta == 'a':
                aciertos += 1
            elif respuesta == 'e':
                errores += 1
        indice += 1
    return aciertos,errores

def respuesta_correcta(partida,jugador,indice,palabra_actual,palabra_usuario,jugador_actual,indice_jugador):
    # Hecha por Orlando Martin
    """
    * Función encargada de actualizar los valores del jugador si la respuesta fue correcta
    *
    * Pre: Recibe el diccionario de partida, el jugador participante, su índice, la palabra 
    *   actual que se encuentra participando y la palabra ingresada por el usuario
    * 
    """
    partida[CONFIGURACION['RESUMEN_PARTIDA']] += (f"\nTurno letra {palabra_actual[int(CONFIGURACION['INICIAL'])].upper()} - Jugador {indice_jugador} {jugador} - Palabra de {len(palabra_actual)} - {palabra_usuario} - acierto")
    partida[CONFIGURACION['JUGADOR']][indice] = indice_jugador
    partida[CONFIGURACION['RESULTADOS']][indice] = "a"
    jugador_actual[CONFIGURACION['PUNTAJE_PARTIDA']] += int(CONFIGURACION['PUNTAJE_ACIERTO'])
    jugador_actual[CONFIGURACION['PUNTAJE_GLOBAL']] += int(CONFIGURACION['PUNTAJE_ACIERTO'])
    print("Palabra correcta")
    
def respuesta_incorrecta(partida,jugador,indice,palabra_actual,palabra_usuario,jugador_actual,indice_jugador):
    # Hecha por Orlando Martin
    """
    * Función encargada del flujo de respuesta incorrecta
    *
    * Pre: Recibe el diccionario de partida, el jugador participante, su índice, la palabra actual que se encuentra participando y la palabra ingresada por el usuario
    *
    """
    partida[CONFIGURACION['RESUMEN_PARTIDA']] += (f"\nTurno letra {palabra_actual[int(CONFIGURACION['INICIAL'])].upper()} - Jugador {indice_jugador} {jugador} - Palabra de {len(palabra_actual)} - {palabra_usuario} - error - Palabra correcta: {palabra_actual}")
    partida[CONFIGURACION['JUGADOR']][indice] = indice_jugador
    partida[CONFIGURACION['RESULTADOS']][indice] = "e"
    jugador_actual[CONFIGURACION['PUNTAJE_PARTIDA']] -= int(CONFIGURACION['PUNTAJE_DESACIERTO'])
    jugador_actual[CONFIGURACION['PUNTAJE_GLOBAL']] -= int(CONFIGURACION['PUNTAJE_DESACIERTO'])
    print(f"Palabra incorrecta - Respuesta: {palabra_actual}")

def imprimir_resultados_parciales(partida,jugadores):
    # Hecha por Orlando Martin
    """
    * Función encargada de imprimir los resultados parciales
    *
    * Pre: Recibe el diccionario de partida y el listado de los jugadores participantes
    *
    >>> partida = {'jugador':[1,1,1,2,2,1],'resultados':['a','a','e','a','e','a']}
    >>> jugadores = ['martin','lorenzo']
    >>> imprimir_resultados_parciales(partida,jugadores)
    1. martin - Aciertos: 3 - Errores : 1
    2. lorenzo - Aciertos: 1 - Errores : 1
    """
    numero = 1
    jugadores_turno = partida[CONFIGURACION['JUGADOR']]
    resultados_jugador = partida[CONFIGURACION['RESULTADOS']]
    for jugador in jugadores:
        aciertos,errores = contador_aciertos(resultados_jugador, numero, jugadores_turno)
        print(f"{numero}. {jugador} - Aciertos: {aciertos} - Errores : {errores}")
        numero += 1

def generar_resultados_y_respuestas(letras):
    # Hecha por Nuñez Juan Bautista
    """
    * Funcion encargada de inicializar los resultados
    *
    * Pre: Recibe un listado de letras
    *
    * Post: Retorna la lista de resultados inicializada
    *
    >>> generar_resultados_y_respuestas(['a','b','c','d'])
    ['', '', '', '']
    """
    resultados = []
    for letra in letras:
        resultados.append('')
    return resultados
print(doctest.testmod())
