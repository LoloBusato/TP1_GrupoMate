from etapa_4 import *

def pasapalabra(jugadores,partida):
    #Hecha por Orlando Martin
    """
    *Función que ejecuta cada partida de pasapalabra
    *
    * Pre: Recibe un listado de los jugadores de cada partida y un diccionario que contiene la información global
    *
    *   partida = {
    *       dicionario: [[palabra_1,definicion_1],[palabra_2,definicion_2],...,],
    *       letras:['a','b',...,],
    *       jugador:['','',...,],
    *       resultados:['','',...,],
    *       resumen_partida:'',
    *       nombre_jugador_1:{
    *           puntaje_global: 0,
    *           puntaje_partida: 0
    *       }
    *       nombre_jugador_2:{
    *           ...
    *      }
    *  }
    *   
    * Post: devuelve el diccionario partida modificado con los datos despues del cierre de la partida
    """
    indice_jugador = 0
    numero_jugador = 1
    indice_partida = 0
    while indice_jugador != -1:
        #Ciclo actuante si el jugador actual tiene turno libre o hay alguno que aun tenga turnos libres
        error = False
        jugador = selecciona_jugador(indice_jugador,jugadores)
        if(jugador):
            jugador_actual = partida[jugador]
            diccionario_partida = partida[CONFIGURACION['DICCIONARIO']]
            letras_partida = partida[CONFIGURACION['LETRAS']]
            jugadores_partida = partida[CONFIGURACION['JUGADOR']]
            resultados_partida = partida[CONFIGURACION['RESULTADOS']]
            while (indice_partida < len(letras_partida) and not error):
                # Mientras no se recorra todo el rosco o se equivoque
                resultados,abecedario_imprimir,jugadores_imprimir = iniciar_resultados_abecedario(letras_partida,resultados_partida,jugadores_partida)
                
                palabra_actual = diccionario_partida[indice_partida][int(CONFIGURACION['PALABRA'])]
                definicion_actual = diccionario_partida[indice_partida][int(CONFIGURACION['DEFINICION'])]
                
                imprimir_resultados(abecedario_imprimir,palabra_actual,definicion_actual,partida,jugadores,jugador, numero_jugador)
                
                palabra_usuario = pedir_palabra(len(palabra_actual))
                respuesta = valida_respuesta(palabra_usuario,palabra_actual)
                if respuesta:
                    #partida,jugador,indice,palabra_actual,palabra_usuario
                    respuesta_correcta(partida,jugador,indice_partida,palabra_actual,palabra_usuario,jugador_actual,numero_jugador)
                else:
                    respuesta_incorrecta(partida,jugador,indice_partida,palabra_actual,palabra_usuario,jugador_actual,numero_jugador)
                    error = True
                indice_partida += 1
        print(f"\nFin del turno de {jugador}\n")
        if (indice_partida < int(CONFIGURACION['CANTIDAD_LETRAS_ROSCO'])):
            indice_jugador = incrementa_jugador(len(jugadores),indice_jugador)
            numero_jugador = indice_jugador + 1
        else:
            indice_jugador = -1
    return partida