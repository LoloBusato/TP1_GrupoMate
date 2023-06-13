import csv
import random

#----------------------------------------------------------------------------------------------------------------
#GENERO VARIABLES Y CONSTANTES QUE VOY A USAR
PALABRA=0
MINIMO=4
ENCODING='utf-8'

#-------------------------------------------------------------------------------------------------------------------

#LEE LOS ARCHIVOS.TXT LINEA POR LINEA
def leer_archivos(palabras,definiciones):
    linea_def=definiciones.readline().rstrip()
    linea_pal=palabras.readline().rstrip()
    return linea_pal,linea_def

#CREACION DE NUESTRO DICC ORDENADO ALF.   TYPE: LIST
def crear_diccionario(palabras,definiciones):
    dicc={}
    palabra,definicion=leer_archivos(palabras,definiciones)
    while palabra:
            #valido que la palabra sea alum.
            if palabra.isalnum() and len(palabra)>MINIMO:
                dicc[palabra]="'"+str(definicion)+"'"
            palabra,definicion=leer_archivos(palabras,definiciones)
    dicc=sorted(dicc.items(),key=lambda x:x[PALABRA])
    return dicc

#------------------------------------------------------------------------------------------------------------------------

#CREO EL ARCHIVO DICCIONARIO.CSV
def crear_diccionario_csv(palabras,definiciones):
    palabras_definiciones=crear_diccionario(palabras,definiciones)
    diccionario_csv = 'diccionario.csv'
    #escribir los datos en el archivo CSV
    with open(diccionario_csv, 'w', newline='',encoding=ENCODING) as dicc_csv:
        escritor = csv.writer(dicc_csv)
        escritor.writerows(palabras_definiciones)

def leer_archivo_diccionario(diccionario_txt):
    linea=diccionario_txt.readline().rstrip()
    return linea.split(',') if linea else ('','')

def leer_diccionario(diccionario_csv):
    diccionario_lista = []
    palabra_definicion = leer_archivo_diccionario(diccionario_csv)
    while palabra_definicion != ('', ''):
        while len(palabra_definicion) > 2:
            palabra_definicion[-2:] = [palabra_definicion[-2] + "," + palabra_definicion[-1]]
        diccionario_lista.append(palabra_definicion)
        palabra_definicion = leer_archivo_diccionario(diccionario_csv)
    return diccionario_lista
    

def obtener_lista_definiciones():
    #ABRIMOS LOS ARCHIVOS.TXT--------------------------------------------------------------------------------------------
    palabras_txt = open('palabras.txt', 'r', encoding=ENCODING)
    definiciones_txt = open('definiciones.txt', 'r', encoding=ENCODING)
    crear_diccionario_csv(palabras_txt,definiciones_txt)
    #CIERRO LOS ARCHIVOS TXT--------------------------------------------------------------------------------------------
    palabras_txt.close()
    definiciones_txt.close()
    diccionario_csv = open('diccionario.csv', 'r', encoding=ENCODING)
    diccionario_lista = leer_diccionario(diccionario_csv)
    diccionario_csv.close()
    random.shuffle(diccionario_lista)
    return diccionario_lista



