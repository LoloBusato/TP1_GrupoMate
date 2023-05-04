"""
En esta etapa deberás escribir las funciones que consideres
necesarias, y que permitan una interacción con el jugador, y
que sigan los lineamientos que se dan a continuación.

Inicialmente, comenzaremos por mostrar el tablero con las
letras participantes, debajo de cada letra se mostrará el
resultado de haber adivinado la palabra de dicha letra, siendo
“a” de acierto, o bien “e” de error.
Al usuario se le debe indicar el turno actual, la cantidad de
letras de la palabra a adivinar y la definición de la misma.

Una vez que el usuario ingrese la palabra se le indicará si fue
correcta o no, y en el caso de ser incorrecta se le muestra la
palabra correcta. Y luego se pasa al siguiente turno de letra.

Cuando la palabra es ingresada por el usuario debe validarse que
esté compuesta sólo por letras, no están permitidos los números,
espacios ni ningún carácter especial, y que sea de la longitud
correcta para el turno.
"""
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

def valida_respuesta (aciertos,errores,indice,palabra,resultados):
    """
    Se pide al usuario que ingrese su respuesta y se realiza la validacion
    asi como tambien se actualizar las variables que dependen de la respuesta
    """
    respuesta = input("Ingrese palabra: ")
    while not respuesta.isalpha():
        print("Respuesta inválida, intente nuevamente")
        respuesta = input("Ingrese palabra: ")    
    if (len(palabra) == len(respuesta) and palabra.lower() == respuesta.lower()):
        resultados[indice]="a"
        aciertos += 1
        print("Palabra correcta")
    else:
        print(f"Palabra incorrecta - Respuesta: {palabra}")
        resultados[indice]="e"
        errores += 1
    return (aciertos,errores)

def impresion_final(aciertos):
    print("-------------------------------------")
    print('Impresion de diccionario y respuestas')
    print(f"Puntaje final: {aciertos}")

def pasapalabras():
    
    """
    Se crean las variables abecedario donde se encuentran todas las letras
    y se le da un formato a las mismas para despues poder imprimirlas.
    """
    ABECEDARIO = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    resultados = []
    abecedario_imprimir = ""
    for letra in ABECEDARIO:
        abecedario_imprimir += f"[{letra}]"
        resultados.append(" ")
        
    
    """
    Se definen algunas variables para realizar pruebas de la interfaz grafica
    """
    aciertos = 0
    errores = 0
    indice = 0
    palabra = "Almuerzo"
    definicion = "1. m. Comida que se toma por la mañana"
    
    """
    Se llama a la funcion que se encarga de imprimir la interfaz al usuario
    """
    while indice < len(ABECEDARIO): 
        imprimir_resultados(abecedario_imprimir, resultados, aciertos, errores, palabra, definicion)
        #valida respuesta y actualiza aciertos y errores
        (aciertos,errores)=valida_respuesta(aciertos,errores,indice,palabra,resultados)
        indice+=1
    impresion_final(aciertos)



#def validar_formato_respuesta(palabra, respuesta):
    #return True if (len(palabra) == len(respuesta) and respuesta.isalpha()) else False
           
pasapalabras()



