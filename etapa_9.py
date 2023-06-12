from pasapalabra import pasapalabra;
def obtener_definiciones():
    pass
def letras_participantes():
    pass
def creacion_diccionarios(jugadores):
    partida = {}
    for jugador in jugadores:
        if jugador not in partida.keys():
            partida[jugador] = {
                'dicionario': []#obtener_definiciones()
                ,
                'letras': []#letras_participantes()
                ,
                'resultados':[],
                'turno': 0,
                'puntaje_partida': 0,
                'resumen_partida':'',
                'puntaje_global': 0,
                
            }
        #El caso contrario no deberia ocurrir nunca
    return partida


def fin_de_partida():
    #impresion de reusltados
    pass

def pedir_continuacion():
    seguir_jugando = True
    continuar = input('¿Desea seguir jugando? Ingrese si o no:')
    while continuar.lower() != 'si' and continuar.lower != "no":
        continuar = input('Error, ¿desea seguir jugando? Ingrese si o no:')
        if continuar.lower == "no":
            seguir_jugando=False
    return seguir_jugando
def main (jugadores):
    '''
    * Función encargada de mantener la dinámica del juego y definir la continuidad del juego
    * Pre: Recibe una lista con los nombres de usuario de los jugadores participantes
    '''
    
    seguir_jugando = True
    while seguir_jugando:
        #Genera diccionarios para cada jugador
        partida = creacion_diccionarios(jugadores)
        
        #inicia los ciclos de pasapalabra hasta el final de la partida
        partida = pasapalabra(jugadores,partida)
        
        #resultados parciales
        
        #pide input del jugador
        seguir_jugando = pedir_continuacion()
        
        #resultados finales
    fin_de_partida()    
    
main()