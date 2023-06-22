import random
from etapa_10 import obtener_constantes

#CONSTANTES=================================================================================================
CONFIGURACION = obtener_constantes()

#FUNCIONES========================================================================================
def leer_archivos(palabras,definiciones):
    # Hecha por Nuñez Juan Bautista
    """
    * Funcion encargada de leer cada linea de los archivos
    *
    * Pre: Recibe 2 archivos abiertos de formato txt que contienen todas las palabras definicion
    *
    * Post: devuelve la siguiente linea de los archivos que contienen las palabras y definiciones
    *       
    """
    linea_def = definiciones.readline().rstrip()
    linea_pal = palabras.readline().rstrip()
    return linea_pal,linea_def

def crear_diccionario(palabras,definiciones):
    # Hecha por Nuñez Juan Bautista
    """
    * Funcion encargada de crear un diccionario con las palabras,definiciones
    *
    * Pre: recibe 2 archivos abiertos en formato .txt ordenados por linea
    *
    * Post: devuelve un diccionario con todas las definiciones y palabras con formato
    *   
    *       
    """
    dicc = {}
    palabra,definicion = leer_archivos(palabras,definiciones)
    while palabra:
            if palabra.isalpha() and len(palabra) > int(CONFIGURACION['LONGITUD_PALABRA_MINIMA']):
                dicc[palabra] = definicion
            palabra,definicion=leer_archivos(palabras,definiciones)
    dicc = sorted(dicc.items(),key=lambda x:x[int(CONFIGURACION['PALABRA'])])
    return dicc


def crear_diccionario_csv(palabras,definiciones,diccionario):
    # Hecha por Nuñez Juan Bautista
    """
    * Funcion encargada de crear un archivo csv con las palabras, definicion
    *
    * Pre: Recibe 2 archivos abiertos de formato txt que contienen todas las palabras definicion
    *   y 1 archivo abierto vacio en modo escritura
    *       
    """
    palabras_definiciones=crear_diccionario(palabras,definiciones)
    for palabra_definicion in palabras_definiciones:
        diccionario.write(palabra_definicion[int(CONFIGURACION['PALABRA'])] + ','  + palabra_definicion[int(CONFIGURACION['DEFINICION'])] + "\n")
    

def leer_archivo_diccionario(diccionario_txt):
    # Hecha por Nuñez Juan Bautista
    """
    * Funcion encargada de leer cada linea del archivo diccionario.txt
    *
    * Pre: Recibe 1 archivo abierto en formato .txt
    *
    * Post: devuelve como lista una linea del archivo     
    """
    linea = diccionario_txt.readline().rstrip()
    return linea.split(',') if linea else ('','')


def leer_diccionario(diccionario_csv):
    # Hecha por Nuñez Juan Bautista
    """
    * Funcion encargada procesar el archivo diccionario_csv creado
    *
    * Pre: Recibe 1 archivo abierto en formato .csv
    *
    * Post: devuelve una lista con las palabras definiciones en formato
    *   [
    *       [palabra, definicion],
    *       ... 
    *   ]
    *
    """
    diccionario_lista = []
    palabra_definicion = leer_archivo_diccionario(diccionario_csv)
    while palabra_definicion != ('', ''):
        while len(palabra_definicion) > 2:
            palabra_definicion[-2:] = [palabra_definicion[-2] + "," + palabra_definicion[-1]]
        diccionario_lista.append(palabra_definicion)
        palabra_definicion = leer_archivo_diccionario(diccionario_csv)
    return diccionario_lista
    

def obtener_lista_definiciones():
    # Hecha por Nuñez Juan Bautista
    """
    * Funcion encargada de abrir los archivos, cerrarlos y devolver las palabras, diccionario
    *   en formato lista mezcladas
    *
    * Post: devuelve una lista con las palabras definiciones en formato
    *   [
    *       [palabra, definicion],
    *       ... 
    *   ]
    *
    """
    #ABRIMOS LOS ARCHIVOS.TXT--------------------------------------------------------------------------------------------
    palabras_txt = open('palabras.txt', 'r', encoding=CONFIGURACION['ENCODING'])
    definiciones_txt = open('definiciones.txt', 'r', encoding=CONFIGURACION['ENCODING'])
    diccionario_csv = open('diccionario.csv','w',encoding=CONFIGURACION['ENCODING'])
    #PROCESADO DE DATOS------------------------------------------------------------------------------
    crear_diccionario_csv(palabras_txt,definiciones_txt,diccionario_csv)
    #CIERRO LOS ARCHIVOS TXT--------------------------------------------------------------------------------------------
    palabras_txt.close()
    definiciones_txt.close()
    diccionario_csv = open('diccionario.csv', 'r', encoding=CONFIGURACION['ENCODING'])
    diccionario_lista = leer_diccionario(diccionario_csv)
    diccionario_csv.close()
    random.shuffle(diccionario_lista)
    return diccionario_lista
