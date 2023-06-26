from pasapalabra import pasapalabra
from etapa_4 import *
from Etapa_8 import obtener_lista_definiciones
from etapa_7 import *
from etapa_10 import obtener_constantes
import random
import doctest

#CONSTANTES========================================================================================================
CONFIGURACION = obtener_constantes()
#FUNCIONES=======================================================================================================
def obtener_definiciones(dicc,letras):
    # Hecha por Nuñez Juan Bautista
    """
    * funcion obtener_definiciones - acepta una lista con [palabra,definicion] y una lista de letras
    *   devuelve unicamente una lista con una palabra, definicion por letra
    *
    * pre: dicc es una lista con formato [palabra, definicion] y letras es una lista de letras
    *
    * post: devuelve la variable definciones con formato
    *       [
    *           (palabra, definicion),
    *           (palabra, definicion),
    *           ...
    *       ]
    """
    cont_letra = 0
    cont_dicc = 0
    lista_candidatos = []
    palabras_definiciones = []
    while cont_letra < len(letras):
        if letras[cont_letra] == dicc[cont_dicc][int(CONFIGURACION['INICIAL'])]:
            lista_candidatos = dicc[cont_dicc][int(CONFIGURACION['DEFINICION'])]
            random.shuffle(lista_candidatos)
            palabras_definiciones.append(lista_candidatos[int(CONFIGURACION['PRIMERA_PALABRA_DEFINICION'])])
            cont_letra += 1
            cont_dicc = 0
        cont_dicc += 1
    return palabras_definiciones
        



def creacion_diccionarios(jugadores, partida, cant_partidas):
    # Hecha por Nuñez Juan Bautista
    """
    * Funcion encargada de crear un diccionario por cada jugador de la partida
    *
    * Pre: Recibe una lista con los nombres de los jugadores 
    *
    * Post: Retorna un diccionario con formato
        partida = {
            diccionario: [[palabra_1,definicion_1],[palabra_2,definicion_2],...,],
            letras:['a','b',...,],
            jugador:['','',...,],
            resultados:['','',...,],
            resumen_partida:'',
            nombre_jugador_1:{
                puntaje_global: 0,
                puntaje_partida: 0
            }
            nombre_jugador_2:{
                ...
            }
        }
    *
    """
    diccionario_lista = obtener_lista_definiciones()
    letras = letras_participantes()
    dicc_definiciones = obtener_definiciones(diccionario_lista,letras)
    resultados = generar_resultados_y_respuestas(letras)
    jugador_partida = generar_resultados_y_respuestas(letras)

    partida[CONFIGURACION['DICCIONARIO']] = dicc_definiciones
    partida[CONFIGURACION['LETRAS']] = letras
    partida[CONFIGURACION['JUGADOR']] = jugador_partida
    partida[CONFIGURACION['RESULTADOS']] = resultados
    partida[CONFIGURACION['RESUMEN_PARTIDA']] = ''

    for jugador in jugadores:
        if cant_partidas == 1:
            partida[jugador] = {}
            partida[jugador][CONFIGURACION['PUNTAJE_GLOBAL']] = 0        
        partida[jugador][CONFIGURACION['PUNTAJE_PARTIDA']] = 0
    return partida

def resultados_parciales(jugadores,partida):
    # Hecha por Nuñez Juan Bautista
    """
    * Funcion encargada de imprimir los resultados parciales de los jugadores
    *
    * Pre: Recibe una lista con los nombres de los jugadores y el diccionario con la informacion
    *   de la partida con formato
    *   {
    *       jugador1: {...},
    *       jugador2: {...},
    *       ...
    *   }
    *
    * Post: imprime informacion al usuario del estado parcial de la partida con formato
    *   "X. JugadorX - Aciertos: X - Errores: X"
    *
    """
    print(f'{partida[CONFIGURACION["RESUMEN_PARTIDA"]]}\n\n')
    print('Puntaje de la partida:')
    count = 0
    for jugador in jugadores:
        count += 1
        print(f'{count}. {jugador} - {partida[jugador][CONFIGURACION["PUNTAJE_PARTIDA"]]} puntos') 
    print('\n\n')
    print('Puntaje parcial:')
    count = 0
    for jugador in jugadores:
        count += 1
        print(f'{count}. {jugador} - {partida[jugador][CONFIGURACION["PUNTAJE_GLOBAL"]]} puntos') 
    return ()

def fin_de_partida(jugadores,partida,cant_partida):
    # Hecha por Nuñez Juan Bautista
    """
    * Funcion encargada de imprimir los resultados finales de los jugadores
    *
    * Pre: Recibe una lista con los nombres de los jugadores, el diccionario con la informacion
    *   de la partida con formato
    *   {
    *       jugador1: {...},
    *       jugador2: {...},
    *       ...
    *   }
    *   y un numero con la cantidad de partidas jugadas en total
    *
    * Post: imprime los resultados finales de la partida con formatos
    *   "X. JugadorX - PUNTAJE"
    *       
    *
    >>> jugadores = ['martin', 'lorenzo']
    >>> cantidad_partidas = 1
    >>> partida = {'diccionario':['def-1','def-2','def de circuito','def-4'],'letras':['a','b','c','d'],'jugador':[1,1,' ',' '],'resultados':['a','a',' ',' '],'resumen_partida':'asd','martin':{'puntaje_partida':10,'puntaje_global':30},'lorenzo':{'puntaje_partida':20,'puntaje_global':40}}
    >>> fin_de_partida(jugadores, cantidad_partidas, partida)
    Reporte Final:
    Partidas jugadas: 1
    <BLANKLINE>
    <BLANKLINE>
    Puntaje final:
    1. martin - 30 puntos
    2. lorenzo - 40 puntos
    """
    print('Reporte Final:')
    print(f'Partidas jugadas: {cant_partida} \n\n')
    print('Puntaje final:')
    count = 0
    for jugador in jugadores:
        count += 1
        print(f'{count}. {jugador} - {partida[jugador][CONFIGURACION["PUNTAJE_GLOBAL"]]} puntos') 

def pedir_continuacion():
    # Hecha por Nuñez Juan Bautista
    """
    * Funcion encargada de obtener la informacion si el jugador quiere seguir jugando o no
    *
    * Post: devuelve un booleano indicando si el jugador quiere seguir jugando o no
    *       
    *
    """
    seguir_jugando = True
    continuar = input('¿Desea seguir jugando? Ingrese si o no: ')
    while continuar.lower() != 'si' and continuar.lower() != "no":
        continuar = input('Error, ¿desea seguir jugando? Ingrese si o no: ')
    if continuar.lower() == "no":
        seguir_jugando = False
    return seguir_jugando

#CUERPO FUNCION PRINCIPAL===============================================================================================================
def main():
    # Hecha por Nuñez Juan Bautista y Orlando Martin
    """
    * Función encargada de iniciar la dinámica del juego y definir la continuidad del mismo
    """
    cant_partidas = 0
    jugadores = ventana_de_jugadores()
    seguir_jugando = True
    partida = {}
    while seguir_jugando and cant_partidas < int(CONFIGURACION['MAXIMO_PARTIDAS']) and len(jugadores) >= 1:
        cant_partidas += 1

        #Genera diccionarios para cada jugador
        partida = creacion_diccionarios(jugadores,partida, cant_partidas)
        
        #inicia los ciclos de pasapalabra hasta el final de la partida
        partida = pasapalabra(jugadores,partida)
        
        #resultados parciales
        resultados_parciales(jugadores,partida)

        #pide continuacion del juego
        seguir_jugando = pedir_continuacion()
    fin_de_partida(jugadores,partida,cant_partidas)


main()
