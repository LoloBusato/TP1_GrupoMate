"""En esta etapa debemos integrar las funcionalidades resueltas en cada una de las etapas
anteriores, haciendo un uso adecuado de las funciones escritas.
La secuencia del juego debe ser la siguiente:
1. Se deberá comenzar con la generación del diccionario de palabras.
2. Luego se deben seleccionar las 10 letras participantes.
3. El programa elegirá al azar la lista de palabras a adivinar por el jugador.
4. Luego se armará el tablero que visualizará el usuario, y dará comienzo la partida,
implementando así, lo realizado en la etapa 1."""
def partida_pasapalabra(puntaje = 0):
    PUNTAJE_ACIERTO = 10
    PUNTAJE_ERROR = 3
    #1. Se deberá comenzar con la generación del diccionario de palabras.
    from etapa_2 import obtener_definiciones
    definiciones = obtener_definiciones()
    print(definiciones)

    #2. Luego se deben seleccionar las 10 letras participantes.
    #defino una funcion que lo haga:
    CANTIDAD_LETRAS_ROSCO = 10
    import random
    def letras_participantes():
        letras_rosco= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
        random.shuffle(letras_rosco)
        return sorted(letras_rosco[:CANTIDAD_LETRAS_ROSCO])
    letras= letras_participantes()

    #3. El programa elegirá al azar la lista de palabras a adivinar por el jugador.
    from etapa_3 import palabras_del_rosco
    palabras_seleccionadas= palabras_del_rosco(definiciones, letras)

    #4. Luego se armará el tablero que visualizará el usuario, y dará comienzo la partida,
    #implementando así, lo realizado en la etapa 1.

    def formateo_resultados(resultados):
        '''
        Recibe la lista de resultados y las pasa a un formato amigable para la consola. Retorna un string con formato
        '''
        resultados_a_imprimir = ""
        for letra in resultados:
            if letra:
                resultados_a_imprimir +=f"[{letra}]"
            else:
                resultados_a_imprimir +=f"[ ]"
        return resultados_a_imprimir
    def imprimir_resultados(abecedario_imprimir, resultados, aciertos, errores, palabra, definicion):
        """
        Funcion encargada de imprimir el rosco en pantalla
        """
        print(abecedario_imprimir)
        resultado_imprimir = formateo_resultados(resultados)
        print(resultado_imprimir + "\n\n")
        
        print(f"Aciertos: {aciertos}")
        print(f"Errores: {errores}")
        
        print(f"Turno letra {palabra[0]} - Palabra de {len(palabra)} letras")

        print(f"Definición: {definicion}")

    def valida_respuesta (palabra):
        valida = False
        respuesta = input("Ingrese palabra: ")
        while not respuesta.isalpha():
            print("Respuesta inválida, intente nuevamente")
            respuesta = input("Ingrese palabra: ")
        if (len(palabra) == len(respuesta) and palabra.lower() == respuesta.lower()):
            valida = True            
        return valida


    def impresion_final(aciertos):
        print("-------------------------------------")
        print('Impresion de diccionario y respuestas')
        print(f"Cantidad de aciertos: {aciertos}")

    #esta funcion recorre la lista de palabras seleccionadas y me las va pasando una a una.
    def palabras(count):
        palabra= palabras_seleccionadas[count]
        return palabra

    #idem de la anterior pero con sus respectivas definiciones.
    def funcion_definiciones (count):
        palabra= palabras_seleccionadas[count]
        definicion= definiciones[palabra]
        return definicion


    """
    Se crean las variables abecedario donde se encuentran todas las letras
    y se le da un formato a las mismas para despues poder imprimirlas.
    """
    LETRAS = letras
    resultados = []
    abecedario_imprimir = ""
    for letra in LETRAS:
        abecedario_imprimir += f"[{letra}]"
        resultados.append(" ")
    
    
    """
    Se definen algunas variables para realizar pruebas de la interfaz grafica
    """
    aciertos = 0
    errores = 0
    count = 0                
    """
    Se llama a la funcion que se encarga de imprimir la interfaz al usuario
    """
    while count < len(LETRAS):
        imprimir_resultados(abecedario_imprimir, resultados, aciertos, errores, palabras(count), funcion_definiciones(count))
        respuesta = valida_respuesta(palabras(count))
        if respuesta:
            aciertos +=1
            resultados[count]="a"
            puntaje += PUNTAJE_ACIERTO
            print("Palabra correcta")
            count +=1
        else:
            errores +=1
            resultados[count]= "e"
            puntaje -= PUNTAJE_ERROR
            print (f"Palabra incorrecta - Respuesta: {palabras(count)}")
            count+=1
    impresion_final(aciertos)
    return puntaje








