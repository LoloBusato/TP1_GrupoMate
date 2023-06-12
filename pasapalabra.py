from etapa_4 import *

def pasapalabra(jugadores,partida):
    #Hecha por Orlando Martin
    '''
    Función que ejecuta cada partida de pasapalabra
    
    * Pre: Recibe un listado de los jugadores de cada partida y un diccionario que contiene la información global
    
        partida={
            'dicionario': lista de definiciones en orden de rosco,
            'letras': lista de letras en orden de rosco,
            'resultados': lista de 'a' || 'e' segun acierto o error
            'turno': numero de turno en funcion a la posicion en letras correspondiente,
            'puntaje_partida': 0,
            'resumen_partida': en string el resumen de la partida
            'puntaje_global': 0,
        }
    * Post: devuelve el diccionario partida modificado con los datos despues del cierre de la partida
    '''
    indice_jugador = busca_siguiente_turno_libre(partida,jugadores)
    while indice_jugador != -1:
        #Ciclo actuante si el jugador actual tiene turno libre o hay alguno que aun tenga turnos libres
        error = False
        jugador = selecciona_jugador(indice_jugador,jugadores)
        turno = partida[jugador]
        diccionario_partida = turno[DICCIONARIO]
        letras_partida = turno[LETRAS]
        resultados_partida = turno[RESULTADOS]
        indice_partida =turno[TURNO]
        while (indice_partida<len(letras_partida) and not error):
            #Mientras no se recorra todo el rosco o se equivoque
            resultados,abecedario_imprimir = iniciar_resultados_abecedario(letras_partida,resultados_partida)
            aciertos,errores = contador_aciertos(resultados_partida)
            
            palabra_actual = diccionario_partida[indice_partida][0]
            definicion_actual = diccionario_partida[indice_partida][1]
            
            imprimir_resultados(abecedario_imprimir,resultados,aciertos,errores,palabra_actual,definicion_actual,partida,jugadores,jugador)
            
            palabra_usuario = pedir_palabra(len(palabra_actual))
            respuesta = valida_respuesta(palabra_usuario,palabra_actual)
            if respuesta:
                #partida,jugador,indice,palabra_actual,palabra_usuario
                respuesta_correcta(partida,jugador,indice_partida,palabra_actual,palabra_usuario)
            else:
                respuesta_incorrecta(partida,jugador,indice_partida,palabra_actual,palabra_usuario)
                error = True
            indice_partida+=1
            partida[jugador][TURNO]+=1
        print(f"\nFin del turno de {jugador}\n")
        indice_jugador = busca_siguiente_turno_libre(partida,jugadores,indice_jugador)
    return partida

jugadores = ['martin','juan']
partida = {
    'martin':{
        'diccionario':[['anda','def_1'],['boca','def_2'],['casa','def_3'],['dedo','def_4']],
        'letras':['a','b','c','d'],
        'resultados':['a','','',''],
        'turno':1,
        'puntaje_partida':3,
        'resumen_partida':'acierto',
        'puntaje_global':0
        
    },
    'juan':{
        'diccionario':[['esto','def_1'],['funciona','def_2'],['gana','def_3'],['hola','def_4']],
        'letras':['e','f','g','h'],
        'resultados':['','','',''],
        'turno':0,
        'puntaje_partida':0,
        'resumen_partida':'',
        'puntaje_global':0

    }
}
pasapalabra(jugadores,partida)