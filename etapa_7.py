from tkinter import *
from tkinter import messagebox
import csv
from etapa_10 import obtener_constantes
import random


#CONSTANTES=================================================================================
CONFIGURACION = obtener_constantes()

CARACTERES_ESPECIALES= ['#','!']

# Lista de usuarios participantes
jugadores = []

#FUNCIONES=================================================================================
def usuarios_participantes(usuario):
    # Hecha por Luciano Vicini
    """
    * Esta funcion se encarga de revisar si el usuario ingresado ya habia sido ingresado o no
    *
    * Pre: una cadena de caracteres con el nuevo usuario
    *
    * Post: revisa si el nuevo usuario ya se encuentra en la lista de jugadores, en caso
    *   de ya encontrarse devuelve un error, sino lo agrega a la lista y devuelve una alerta
    """
    if usuario in jugadores:
        resultado = messagebox.showerror(message='Este jugador ya esta participando')
    else:
        jugadores.append(usuario)
        resultado = messagebox.showinfo(message=f'{usuario} participará del juego')
    return resultado

def iniciar_partida(raiz):
    # Hecha por Luciano Vicini
    """
    * Esta funcion se encarga de que se cierre el programa pero mantengas la lista de jugadores
    *
    * Pre: recibe la raiz de la interfaz grafica
    *
    """
    raiz.destroy()

def validar_usuario(usuario):
    # Hecha por Luciano Vicini
    """
    * Esta funcion se encarga de revisar si el nombre de usuario cumple con los requisitos
    *   establecidos
    *
    * Pre: recibe una cadena de caracteres correspondiente al usuario
    *
    * Post: devuelve un valor booleano dependiendo si el nombre de usuario cumple o no con
    *   las restricciones
    *
    """
    indice = 0
    validacion = True
    while indice < len(usuario) and validacion:
        if usuario[indice].isalnum() or usuario[indice] == '-':
            indice += 1
        else:
            validacion= False
    return validacion and int(CONFIGURACION['MIN_LONG_USUARIO']) <= len(usuario) and len(usuario) <= int(CONFIGURACION['MAX_LONG_USUARIO'])

def validar_contrasenia(contrasenia):
    # Hecha por Luciano Vicini
    """
    * Esta funcion se encarga de revisar si la contrasenia cumple con los requisitos
    *   establecidos
    *
    * Pre: recibe una cadena de caracteres correspondiente a la contrasenia
    *
    * Post: devuelve un valor booleano dependiendo si la contrasenia cumple o no con
    *   las restricciones
    *
    """
    cont_especiales= 0
    cont_num = 0
    cont_minus = 0
    cont_mayus = 0
    indice = 0
    validacion = True
    while indice < len(contrasenia) and validacion:
        if contrasenia[indice] in CARACTERES_ESPECIALES:
            cont_especiales += 1
        elif contrasenia[indice].isnumeric():
            cont_num += 1
        elif contrasenia[indice].islower():
            cont_minus += 1
        elif contrasenia[indice].isupper():
            cont_mayus += 1
        else:
            validacion = False
        indice += 1
    return validacion and cont_mayus >= int(CONFIGURACION['CONTEO_MINIMO']) and cont_minus >= int(CONFIGURACION['CONTEO_MINIMO']) and cont_num >= int(CONFIGURACION['CONTEO_MINIMO']) and cont_especiales >= int(CONFIGURACION['CONTEO_MINIMO']) and int(CONFIGURACION['MIN_LONG_CONTRASENIA']) <= len(contrasenia) and len(contrasenia) <= int(CONFIGURACION['MAX_LONG_CONTRASENIA'])
    
def iniciar_sesion(usuario, contrasenia, nombre_usuario_entry, contrasenia_entry, raiz):
    # Hecha por Luciano Vicini
    """
    * Esta funcion se encarga de revisar si el usuario y contrasenia ingresados corresponden
    *   a un usuario ya registrado
    *
    * Pre: recibe 2 cadenas de caracteres correspondientes al usuario y a la contrasenia.
    *   los recuadros de input y la ventana de iniciar usuarios
    *
    * Post: devuelve una variable resultado con mensajes de error en caso de no haber sido 
    *   correctos los datos ingresados o con la modificacion en la lista de usuarios participantes
    *   en caso de encontrarse registrado el usuario
    """
    with open('usuarios.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        cont = 0
        for fila in lector:
            if fila[int(CONFIGURACION['USUARIO'])] == usuario:
                if fila[int(CONFIGURACION['CONTRASENIA'])] == contrasenia:
                    cont = -1
                    resultado = usuarios_participantes(usuario)
                    
                    nombre_usuario_entry.delete(0,len(usuario))
                    contrasenia_entry.delete(0,len(contrasenia))
                    if len(jugadores) == 4:
                        raiz.destroy()
                else:
                    cont = 1
        if cont == 1:
            resultado = messagebox.showerror(message='Contrasenia incorrecta')
        elif cont == 0:
            resultado = messagebox.showerror(message='Este usuario no esta registrado')
    return resultado

def registro(usuario,contrasenia, registro):
    # Hecha por Luciano Vicini
    """
    * Esta funcion se encarga de registrar un nuevo usuario
    *
    * Pre: recibe 2 cadenas de caracteres correspondientes al usuario y a la contrasenia y
    *   la raiz de la ventana de registro
    *
    * Post: devuelve una variable resultado con mensajes de error en caso de que el usuario
    *   ya haya sido creado o las credenciales no cumplan con los requisitos o un mensajes
    *   de informacion en caso del usuario crearse correctamente
    """    
    cont = TRUE
    with open('usuarios.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[int(CONFIGURACION['USUARIO'])] == usuario:
                cont = FALSE
    if cont == TRUE:
        if validar_usuario(usuario) and validar_contrasenia(contrasenia):
            with open('usuarios.csv','a',newline='\n') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow([usuario,contrasenia])
                resultado = messagebox.showinfo(message= 'Has sido registrado exitosamente')
                registro.destroy()
        else:
            resultado = messagebox.showerror(message= '''Ingrese un nombre de usuario o contrasenia validos    (NOMBRE DE USUARIO entre 4 y 20 caracteres con -, letras, numeros)   (CONTRASENIA: longitud entre 6 y 12 caracteres, por lo menos 1 mayus,minus,numero y alguno de los siguientes elementos: #, !)''')     
    else:
        resultado = messagebox.showerror(message= 'Este usuario ya se encuentra registrado') 
    return resultado

def registrarse():
    # Hecha por Luciano Vicini
    """
    * Esta funcion se encarga del registro de nuevos usuarios
    """
    Registro= Tk()
            
    Registro.config(background='lightyellow',width='400',height='180')
    Registro.title('Registro de Usuario')
    
    R_nombre_usuario_entry= Entry(Registro)
    R_nombre_usuario_entry.place(x= 200, y=40)
    R_contrasenia_entry= Entry(Registro)
    R_contrasenia_entry.place(x=200, y= 80)
    R_contrasenia_entry.config(show= '*')

    R_nombre_usuario_label= Label(Registro, text= 'Nombre de Usuario:', bg='lightyellow')
    R_nombre_usuario_label.place(x=70, y=40)
    R_contrasenia_label= Label(Registro, text= 'Contrasenia:', bg='lightyellow')
    R_contrasenia_label.place(x=115, y= 80)
    
    R_registrarse_boton= Button(Registro,text= 'Registrarse',command= lambda:registro(R_nombre_usuario_entry.get(),R_contrasenia_entry.get(), Registro))
    R_registrarse_boton.place(x=150, y= 120)
    
    Registro.mainloop()
    
def ventana_de_jugadores():
    # Hecha por Vicini Luciano
    """
    * Funcion encargada de crear la interfaz grafica para el registro, inicio y almacenamiento de usuarios
    *
    * Post: devuelve una lista con los nombres de usuario de los jugadores ingresados
    *       
    """
    raiz= Tk()

    raiz.config(background='lightblue',width='400',height='250')
    raiz.title('Ingreso de Usuarios')
    raiz.resizable(0,0)

    nombre_usuario_entry= Entry(raiz)
    nombre_usuario_entry.place(x= 200, y=40)
    contrasenia_entry= Entry(raiz)
    contrasenia_entry.place(x=200, y= 80)
    contrasenia_entry.config(show= '*')

    nombre_usuario_label= Label(raiz, text= 'Nombre de Usuario:', bg='lightblue')
    nombre_usuario_label.place(x=70, y=40)
    contrasenia_label= Label(raiz, text= 'Contrasenia:', bg='lightblue')
    contrasenia_label.place(x=115, y= 80)

    iniciar_partida_boton= Button(raiz,text='Iniciar Partida',command= lambda: iniciar_partida(raiz), padx=20)
    iniciar_partida_boton.place(x=130, y= 220)
    iniciar_sesion_boton= Button(raiz,text='Iniciar Sesion',command= lambda: iniciar_sesion(nombre_usuario_entry.get(), contrasenia_entry.get(), nombre_usuario_entry, contrasenia_entry, raiz))
    iniciar_sesion_boton.place(x=150, y= 120)
    registrarse_txt= Label(raiz, text= 'Si no tenes cuenta presiona en el boton de abajo', bg='lightblue', fg= 'blue')
    registrarse_txt.place(x=60, y= 150)
    registrarse_boton= Button(raiz,text= 'Registrarse',command= lambda: registrarse())
    registrarse_boton.place(x=156, y=180)

    raiz.mainloop()
    random.shuffle(jugadores)
    return jugadores
