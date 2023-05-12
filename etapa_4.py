"""En esta etapa debemos integrar las funcionalidades resueltas en cada una de las etapas
anteriores, haciendo un uso adecuado de las funciones escritas.
La secuencia del juego debe ser la siguiente:
1. Se deberá comenzar con la generación del diccionario de palabras.
2. Luego se deben seleccionar las 10 letras participantes.
3. El programa elegirá al azar la lista de palabras a adivinar por el jugador.
4. Luego se armará el tablero que visualizará el usuario, y dará comienzo la partida,
implementando así, lo realizado en la etapa 1."""

#1. Se deberá comenzar con la generación del diccionario de palabras.
from etapa_2 import definiciones

#2. Luego se deben seleccionar las 10 letras participantes.
#defino una funcion que lo haga:

import random
def letras_participantes():
    letras_rosco= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    random.shuffle(letras_rosco)
    return sorted(letras_rosco[0:10])

#3. El programa elegirá al azar la lista de palabras a adivinar por el jugador.
from etapa_3 import palabras_del_rosco
palabras_seleccionadas= palabras_del_rosco(definiciones, letras_participantes())

#4. Luego se armará el tablero que visualizará el usuario, y dará comienzo la partida,
#implementando así, lo realizado en la etapa 1.


def pasapalabras():
    
    """
    Se crean las variables abecedario donde se encuentran todas las letras
    y se le da un formato a las mismas para despues poder imprimirlas.
    """
    LETRAS=letras_participantes()
    abecedario_imprimir = ""
    resultados_imprimir = ""
    for letra in LETRAS:
        abecedario_imprimir += f"[{letra}]"
        resultados_imprimir += "[ ]"
        
    
    """
    Se definen algunas variables para realizar pruebas de la interfaz grafica
    """
    aciertos = 0
    errores = 0
    indice = 0

    """defino una funcion para la correspondiente palabra y su definicion"""
    
    #Se llama a la funcion que se encarga de imprimir la interfaz al usuario
    
    posicion=0
    imprimir_resultados(abecedario_imprimir, resultados_imprimir, aciertos, errores, posicion)
    
    """
    Se pide al usuario que ingrese su respuesta y se realiza la validacion
    asi como tambien se actualizar las variables que dependen de la respuesta
    """
    
    respuesta = input("Ingrese palabra: ")
    if(len(palabra(posicion)) == len(respuesta) and respuesta.isalpha()):
        if (palabra(posicion).lower() == respuesta.lower()):
            print("Palabra correcta")
            aciertos += 1
        else:
            errores += 1
            print(f"Palabra incorrecta - Respuesta: {palabra()}")
        indice +=1
        posicion +=1
    else:
        print("Respuesta no valida")

def palabra(posicion):
    return palabras_seleccionadas(posicion)

def definicion(posicion):
    return definiciones[palabra(posicion)]


def imprimir_resultados(abecedario_imprimir, resultados_imprimir, aciertos, errores,posicion):
        palabra1= palabra(posicion)
        definicion1= definicion(posicion)
        #Funcion encargada de imprimir el rosco en pantalla
        print(abecedario_imprimir)
        print(resultados_imprimir + "\n\n")

        print(f"Aciertos: {aciertos}")
        print(f"Errores: {errores}")

        print(f"Turno letra {palabra1} - Palabra de {len(palabra1)} letras")

        print(f"Definición: {definicion1}")

def validar_formato_respuesta(palabra, respuesta):
    return True if (len(palabra) == len(respuesta) and respuesta.isalpha()) else False

pasapalabras()






