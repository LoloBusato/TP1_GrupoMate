from pasapalabra import pasapalabra
from etapa_4 import *
from etapa_7 import *
from etapa_9 import *
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