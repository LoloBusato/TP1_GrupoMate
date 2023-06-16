from pasapalabra import pasapalabra;
from etapa_4 import *
from Etapa_8 import obtener_lista_definiciones
from etapa_7 import *
import random
#CONSTANTES========================================================================================================
PUNTAJE_PARTIDA = 'puntaje_partida'
RESUMEN_PARTIDA = 'resumen_partida'
PUNTAJE_GLOBAL = 'puntaje_global'
TURNO= 'turno'

#FUNCIONES=======================================================================================================
def obtener_definiciones(dicc,letras):
    definiciones=[]
    palabras_candidatas=[]
    for letra in letras:
        for palabra,definicion in dicc:
            if palabra[0].upper() == letra.upper():
                palabras_candidatas.append((palabra,definicion))
        random.shuffle(palabras_candidatas)
        definiciones.append(palabras_candidatas[0])
    return definiciones

def obtener_resultados(letras):
    count=0
    resultados=[]
    while count<len(letras):
        resultados.append('')
        count +=1
    return resultados

def creacion_diccionarios(jugadores):
    partida = {}
    dicc_global=obtener_lista_definiciones()
    for jugador in jugadores:
        if jugador not in partida.keys():
            letras=letras_participantes()
            dicc_definiciones=obtener_definiciones(dicc_global,letras)
            resultados=obtener_resultados(letras)
            partida[jugador] = {
                DICCIONARIO: dicc_definiciones,
                LETRAS: letras,
                RESULTADOS: resultados,
                TURNO: 0,
                PUNTAJE_PARTIDA: 0,
                RESUMEN_PARTIDA:'',
                PUNTAJE_GLOBAL: 0,
                
            }
        #El caso contrario no deberia ocurrir nunca
    return partida

def resultados_parciales(jugadores,partida):
    print('Puntaje de la partida:\n')
    count=0
    for jugador in jugadores:
        count +=1
        print(f'{count}. {jugador} - {partida[jugador][PUNTAJE_PARTIDA]}') 
    return ()

def fin_de_partida(jugadores,partida,cant_partida):
    print('Reporte Final: \n')
    print(f'Partidas jugadas: {cant_partida} \\n')
    print('Puntaje final: \n')
    for jugador in jugadores:
        count +=1
        print(f'{count}. {jugador} - {partida[jugador][PUNTAJE_GLOBAL]}') 
    return ()

def pedir_continuacion():
    seguir_jugando = True
    continuar = input('¿Desea seguir jugando? Ingrese si o no:')
    while continuar.lower() != 'si' and continuar.lower != "no":
        continuar = input('Error, ¿desea seguir jugando? Ingrese si o no:')
    if continuar.lower == "no":
        seguir_jugando=False
    return seguir_jugando
#CUERPO FUNCION PRINCIPAL===============================================================================================================
def main ():
    '''
    * Función encargada de mantener la dinámica del juego y definir la continuidad del juego
    '''
    cant_partidas=0
    jugadores= ventana_de_jugadores()
    seguir_jugando = True
    while seguir_jugando:
        cant_partidas +=1
        #Genera diccionarios para cada jugador
        partida = creacion_diccionarios(jugadores)
        
        #inicia los ciclos de pasapalabra hasta el final de la partida
        partida = pasapalabra(jugadores,partida)
        
        #resultados parciales
        resultados_parciales(jugadores,partida)
        #pide input del jugador
        seguir_jugando = pedir_continuacion()
            
    return fin_de_partida(jugadores,partida,cant_partidas)

main()