from etapa_4 import *

def pasapalabra(jugadores,partida):
    #Hecha por Orlando Martin
    """
    *Función que ejecuta cada partida de pasapalabra
    *
    * Pre: Recibe un listado de los jugadores de cada partida y un diccionario que contiene la información global
    *
    *   partida={
    *       jugador1: {
    *           'dicionario': lista de definiciones en orden de rosco,
    *           'letras': lista de letras en orden de rosco,
    *           'resultados': lista de 'a' || 'e' segun acierto o error
    *           'turno': numero de turno en funcion a la posicion en letras correspondiente,
    *           'puntaje_partida': 0,
    *           'resumen_partida': en string el resumen de la partida
    *           'puntaje_global': 0,
    *       },
    *       jugador2: {
    *           ...
    *       }, 
    *       ...
    *   }
    * Post: devuelve el diccionario partida modificado con los datos despues del cierre de la partida
    """
    indice_jugador = busca_siguiente_turno_libre(partida,jugadores)
    while indice_jugador != -1:
        #Ciclo actuante si el jugador actual tiene turno libre o hay alguno que aun tenga turnos libres
        error = False
        jugador = selecciona_jugador(indice_jugador,jugadores)
        if(jugador):
            turno = partida[jugador]
            diccionario_partida = turno[CONFIGURACION['DICCIONARIO']]
            letras_partida = turno[CONFIGURACION['LETRAS']]
            resultados_partida = turno[CONFIGURACION['RESULTADOS']]
            indice_partida = turno[CONFIGURACION['TURNO']]
            while (indice_partida < len(letras_partida) and not error):
                # Mientras no se recorra todo el rosco o se equivoque
                resultados,abecedario_imprimir = iniciar_resultados_abecedario(letras_partida,resultados_partida)
                
                palabra_actual = diccionario_partida[indice_partida][int(CONFIGURACION['PALABRA'])]
                definicion_actual = diccionario_partida[indice_partida][int(CONFIGURACION['DEFINICION'])]
                
                imprimir_resultados(abecedario_imprimir,resultados,palabra_actual,definicion_actual,partida,jugadores,jugador)
                
                palabra_usuario = pedir_palabra(len(palabra_actual))
                respuesta = valida_respuesta(palabra_usuario,palabra_actual)
                if respuesta:
                    #partida,jugador,indice,palabra_actual,palabra_usuario
                    respuesta_correcta(partida,jugador,indice_partida,palabra_actual,palabra_usuario)
                else:
                    respuesta_incorrecta(partida,jugador,indice_partida,palabra_actual,palabra_usuario)
                    error = True
                indice_partida+=1
                partida[jugador][CONFIGURACION['TURNO']]+=1
        print(f"\nFin del turno de {jugador}\n")
        indice_jugador = busca_siguiente_turno_libre(partida,jugadores,indice_jugador)
    return partida