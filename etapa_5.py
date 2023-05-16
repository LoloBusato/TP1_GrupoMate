'''
Hasta ahora nuestro jugador, simplemente gana o pierde.
En esta etapa vamos a permitir que obtenga puntaje y que el mismo se acumule de
partida tras partida.
Por cada palabra correcta el usuario suma 10 puntos, por cada palabra incorrecta el
jugador pierde 3 puntos. El puntaje final obtenido podrá ser negativo.
Al finalizar una partida, se le ofrecerá si desea jugar otra; así hasta que responda que
no. El puntaje obtenido en la última partida, se tomará como inicio de la siguiente. Al
inicio de la ejecución del 1er. juego, el puntaje se encuentra en cero.
'''
from etapa_4 import partida_pasapalabra

def pasapalabra ():
    """
    Se definen las variables para el recuento general de puntos
    """
    puntaje = 0
    seguir_jugando = True

    while seguir_jugando:
        puntaje_partida = partida_pasapalabra(puntaje)
        puntaje=puntaje_partida
        continuar = input("Desea seguir jugando? si | no; ")
        while continuar.lower() != "si" and continuar.lower() != "no":
            continuar = input("Error, desea seguir jugando? si | no")
        if continuar.lower() == "no":
            seguir_jugando = False
    #final de partida
    print(f"Final! Su puntaje final fue: {puntaje}")
pasapalabra()