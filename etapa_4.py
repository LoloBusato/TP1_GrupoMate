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
    #Hecha por Orlando Martín
    '''
    * Función que da formato de impresión al listado de resultados
    *
    * Pre: resultados es una lista con valores posibles 'a' en caso de acierto, 'e' en caso de error y ' 'en caso de que no se haya evaluado aún esa respuesta
    *
    * Post: Devuelve un formato de impresión con los mismos valores recibidos
    >>> formateo_resultados(['a','e'])
    '[a][e]'
    >>> formateo_resultados(['e','e','a','a',' ',' '])
    '[e][e][a][a][ ][ ]'
    >>> formateo_resultados([' ',' ',' '])
    '[ ][ ][ ]'
    '''
    resultados_a_imprimir = ""
    for letra in resultados:
        if letra:
            resultados_a_imprimir += f"[{letra}]"
        else:
            resultados_a_imprimir += f"[ ]"
    return resultados_a_imprimir

def reemplaza_tildes(palabra):
    #Hecha por Orlando Martín
    '''
    * Función que reemplaza los tildes de las palabras, de encontrar alguna
    *
    * Pre: Recibe una cadena
    *
    * Post: Devuelve la misma palabra sin tildes
    *
    >>> reemplaza_tildes('esdrújula')
    'esdrujula'
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
    #Hecha por Orlando Martín
    '''
    * Función que evalúa si la palabra otorgada es correcta o no
    
    * Pre: Recibe la palabra ingresada por input por el usuario y la palabra a adivinar 
    
    * Post: Retorna True o False segun la respuesta sea correcta o no
    >>> valida_respuesta('cancion','canción')
    True
    >>> valida_respuesta('perrito','peritos')
    False
    >>> valida_respuesta('pérro','perro')
    False
    '''
    palabra_actual = reemplaza_tildes(palabra_actual)
    respuesta = palabra_usuario.lower() == palabra_actual.lower()
    return respuesta


def iniciar_resultados_abecedario(letras,resultados):
    #Hecha por Orlando Martín
    '''
    * Función que se encarga de iniciar las variables resultados y abecedario_imprimir
    *
    * Pre: recibe "letras" que es una lista ordenada con las letras participantes y "resultados" que es una lista ordenada con los aciertos o errores de cada letra
    *
    * Post: devuelve resultados como una lista con cadenas de caracter vacias y
    *       devuelve abecedario_imprimir con las letras participantes para imprimir
    
    >>> iniciar_resultados_abecedario(["a","b","c","d"],[' ',' ',' ',' '])
    ([' ', ' ', ' ', ' '], '[A][B][C][D]')
    >>> iniciar_resultados_abecedario(["A","f","h","r"],['a','e',' ',' '])
    (['a', 'e', ' ', ' '], '[A][F][H][R]')
    '''
    abecedario_imprimir = ""
    indice = 0
    for letra in letras:
        abecedario_imprimir += f"[{letra.upper()}]"
        if not resultados[indice]:
            resultados[indice]= " "
    return resultados, abecedario_imprimir
def imprimir_resultados(abecedario_imprimir, resultados, palabra, definicion,partida,jugadores,jugador):
    # Hecha por Busato Lorenzo
    """
    * Función que se encarga de la impresión de cada turno del juego y se acciona luego de cada intento 
    *
    * Pre: Recibe las letras participantes ordenadas, los resultados parciales, la palabra del turno, su definición, el contador de partida del jugador, el listado de jugadores y el jugador de turno
    *
    * Post: Imprime el tablero de letras, los resultados parciales, la palabra de turno y su definición
    >>> abecedario_imprimir = "[A][B][C][D]"
    >>> resultados=["a","e"," "," "]
    >>> palabra = "circuito"
    >>> definicion = "def de circuito"
    >>> partida = {'martin':{'diccionario':['def-1','def-2','def de circuito','def-4'],'letras':['a','b','c','d'],'resultados':['a','e',' ',' '],'turno':2,'puntaje_partida':3,'resumen_partida':'asd','puntaje_global':3},'lorenzo':{'diccionario':['def-1','def-2','def de circuito','def-4'],'letras':['a','b','c','d'],'resultados':['a','e',' ',' '],'turno':2,'puntaje_partida':3,'resumen_partida':'asd','puntaje_global':3}}
    >>> jugadores = ['martin','lorenzo']
    >>> jugador = 'martin'
    >>> imprimir_resultados(abecedario_imprimir, resultados, palabra, definicion,partida, jugadores,jugador)
    [A][B][C][D]
    [a][e][ ][ ]
    <BLANKLINE>
    <BLANKLINE>
    Jugadores:
    1. martin - Aciertos: 1 - Errores : 1
    2. lorenzo - Aciertos: 1 - Errores : 1
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    Turno  jugador martin letra C - Palabra de 8 letras
    3. Definición: def de circuito
    """
    print(abecedario_imprimir)
    resultado_imprimir = formateo_resultados(resultados)
    print(resultado_imprimir + "\n\n")
    
    print('Jugadores:')
    imprimir_resultados_parciales(partida,jugadores)
    print("\n\n")
        
    print(f"Turno  jugador {jugador} letra {palabra[0].upper()} - Palabra de {len(palabra)} letras")

    print(f"{partida[jugador][CONFIGURACION['TURNO']]+1}. Definición: {definicion}")
print(doctest.testmod())
def pedir_palabra(longitud):
    # Hecha por Busato Lorenzo
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
    LETRAS_ROSCO= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    random.shuffle(LETRAS_ROSCO)
    return sorted(LETRAS_ROSCO[:int(CONFIGURACION['CANTIDAD_LETRAS_ROSCO'])])

def selecciona_jugador(indice,jugadores):
    #Hecha por Orlando Martin
    '''
    * Función que selecciona un jugador de un listado dependiendo de su índice
    * Pre: Recibe un número, indice, y un listado con todos los jugadores participantes de la partida
    * Post: Retorna el nombre del jugador correspondiente. Si no coresponde seleccionar un jugador, retorna un string vacio
    >>> indice = 3
    >>> jugadores = ['martin','lorenzo','luciano','juan']
    >>> selecciona_jugador(indice,jugadores)
    'juan'
    >>> indice_2 = -1
    >>> selecciona_jugador(indice_2,jugadores)
    ''
    '''
    if (indice == -1):
        jugador = ''
    else: 
        jugador = jugadores[indice]
    return jugador

def incrementa_jugador(cantidad_jugadores,indice=-1):
    #Hecha por Orlando Martin
    '''
    * Función encargada de incrementar el indice de los jugadores reiniciando el ciclo una vez que se halla llegado al final del listado
    * Pre: Recibe un numero indicador de la cantidad de jugadores participantes y el índice actual, siendo -1 el valor por defecto en caso de que no se ingrese como parametro
    * Post: Devuelve un número índice incrementado en uno
    >>> incrementa_jugador(3)
    0
    >>> incrementa_jugador(3,2)
    0
    >>> incrementa_jugador(3,1)
    2
    '''
    indice +=1
    if indice == cantidad_jugadores:
        indice = 0
    return indice

def busca_siguiente_turno_libre(partida,jugadores,indice=-1):
    #Hecha por Orlando Martin
    '''
    * Función encargada de buscar el jugador más cercano con turnos libres para seguir jugando. En caso de no encontrarlo, retorna -1
    * Pre: Recibe el diccionario de partida, un listado de jugadores participantes y el índice correspondiente al jugador participante. De ser el primer jugador participante, se inicializa en -1
    * Post: Retorna el índice del jugador con turnos libres. En caso de no haber ninguno libre, retorna -1
    '''
    ciclos = 0
    libre = False
    indice = incrementa_jugador(len(jugadores),indice)
    while ciclos < len(jugadores) and libre == False:
        jugador = jugadores[indice]
        letras=partida[jugador][CONFIGURACION['LETRAS']]
        turno = partida[jugador][CONFIGURACION['TURNO']]
        if turno < len(letras):
            libre = True
        else:
            indice = incrementa_jugador(len(jugadores),indice)
            ciclos+=1
    return indice if libre else -1


def contador_aciertos(resultados):
    #Hecha por Orlando Martin
    '''
    * Función encargada de contar los aciertos y errores de cada jugador
    * Pre: Recibe un listado con letras 'a', si se registró un acierto, 'e' si se registró un error, y ' ' en caso de que no se haya respondido todavía
    * Post: Retorna una tupla con la cantidad de aciertos y errores del usuario
    >>> contador_aciertos(['a','a','e','a',' '])
    (3, 1)
    >>> contador_aciertos([' ',' ',' ',])
    (0, 0)
    
    '''
    aciertos = 0
    errores = 0
    for respuesta in resultados:
        if respuesta == 'a':
            aciertos +=1
        if respuesta == 'e':
            errores +=1
    return aciertos,errores

def respuesta_correcta(partida,jugador,indice,palabra_actual,palabra_usuario):
    #Hecha por Orlando Martin
    '''
    * Función encargada del flujo de respuesta correcta
    * Pre: Recibe el diccionario de partida, el jugador participante, su índice, la palabra actual que se encuentra participando y la palabra ingresada por el usuario
    
    '''
    partida[jugador]['resumen_partida'] = (f"\nTurno letra{palabra_actual[int(CONFIGURACION['INICIAL'])].upper()} - Palabra de {len(palabra_actual)} - {palabra_usuario} - acierto")
    print("Palabra correcta")
    partida[jugador]['resultados'][indice] = "a"
    partida[jugador]['puntaje_partida'] += int(CONFIGURACION['PUNTAJE_ACIERTO'])
    partida[jugador]['puntaje_global'] += int(CONFIGURACION['PUNTAJE_ACIERTO'])
    
def respuesta_incorrecta(partida,jugador,indice,palabra_actual,palabra_usuario):
    #Hecha por Orlando Martin
    '''
    * Función encargada del flujo de respuesta incorrecta
    * Pre: Recibe el diccionario de partida, el jugador participante, su índice, la palabra actual que se encuentra participando y la palabra ingresada por el usuario
    
    '''
    partida[jugador]['resumen_partida'] = (f"\nTurno letra{palabra_actual[int(CONFIGURACION['INICIAL'])].upper()} - Palabra de {len(palabra_actual)} - {palabra_usuario} - error - Palabra correcta: {palabra_actual}")
    print(f"Palabra incorrecta - Respuesta: {palabra_actual}")
    partida[jugador]['resultados'][indice] = "e"
    partida[jugador]['puntaje_partida'] += int(CONFIGURACION['PUNTAJE_DESACIERTO'])
    partida[jugador]['puntaje_global'] += int(CONFIGURACION['PUNTAJE_DESACIERTO'])

def imprimir_resultados_parciales(partida,jugadores):
    #Hecha por Orlando Martin
    '''
    * Función encargada de imprimir los resultados parciales
    * Pre: Recibe el diccionario de partida y el listado de los jugadores participantes
    >>> partida = {'martin':{'diccionario':['def-1','def-2','def de circuito','def-4'],'letras':['a','b','c','d'],'resultados':['a','e',' ',' '],'turno':2,'puntaje_partida':3,'resumen_partida':'asd','puntaje_global':3},'lorenzo':{'diccionario':['def-1','def-2','def de circuito','def-4'],'letras':['a','b','c','d'],'resultados':['a','e',' ',' '],'turno':2,'puntaje_partida':3,'resumen_partida':'asd','puntaje_global':3}}
    >>> jugadores = ['martin','lorenzo']
    >>> imprimir_resultados_parciales(partida,jugadores)
    1. martin - Aciertos: 1 - Errores : 1
    2. lorenzo - Aciertos: 1 - Errores : 1
    '''
    numero = 1
    for jugador in jugadores:
        resultados_jugador = partida[jugador]['resultados']
        aciertos,errores = contador_aciertos(resultados_jugador)
        print(f"{numero}. {jugador} - Aciertos: {aciertos} - Errores : {errores} ")
        numero+=1
