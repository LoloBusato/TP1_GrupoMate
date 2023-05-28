from etapa_4 import partida_pasapalabra

def pasapalabra ():
    #Hecha por Orlando Martín
    """
    * Función encargada de mantener un puntaje global y definir la continuidad o fin del juego segun el usuario lo desee por comando
    """
    puntaje = 0
    seguir_jugando = True

    while seguir_jugando:
        puntaje_partida = partida_pasapalabra(puntaje)
        puntaje=puntaje_partida
        continuar = input("Desea seguir jugando? si | no: ")
        while continuar.lower() != "si" and continuar.lower() != "no":
            continuar = input("Error, desea seguir jugando? si | no: ")
        if continuar.lower() == "no":
            seguir_jugando = False
    #final de partida
    print(f"Final! Su puntaje final fue: {puntaje}")
pasapalabra()