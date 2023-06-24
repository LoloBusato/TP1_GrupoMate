from tkinter import *
from tkinter import messagebox
import csv
from etapa_10 import obtener_constantes


#CONSTANTES=================================================================================
CONFIGURACION = obtener_constantes()

CARACTERES_ESPECIALES= ['#','!']

# Lista de usuarios participantes
jugadores = []

#FUNCIONES=================================================================================
#esta funcion agrega a la lista de jugadores los nombres de los usuarios a participar
def usuarios_participantes(usuario, jugadores):
    if usuario in jugadores:
        resultado = messagebox.showerror(message='Este jugador ya esta participando')
    else:
        jugadores.append(usuario)
        resultado = messagebox.showinfo(message=f'{usuario} participará del juego')
    return resultado

#esta funcion hace que se cierre el programa pero mantengas la lista de jugadores
def iniciar_partida(raiz):
    raiz.destroy()

#esta funcion comprueba si el nombre de usuario es valido cuando se registra el jugador
def validar_usuario(usuario):
    indice = 0
    validacion= True
    while indice < len(usuario) and validacion==True:
        if usuario[indice].isalnum() or usuario[indice]== '-':
            indice += 1
        else:
            validacion= False
    return validacion and int(CONFIGURACION['MIN_LONG_USUARIO']) <= len(usuario) and len(usuario) <= int(CONFIGURACION['MAX_LONG_USUARIO'])

#esta funcion comprueba si la contrasenia del usuario es valido cuando se registra el jugador
def validar_contrasenia(contrasenia):
    cont_especiales= 0
    cont_num = 0
    cont_minus = 0
    cont_mayus = 0
    indice = 0
    validacion= True
    while indice < len(contrasenia) and validacion==True:
        if contrasenia[indice] in CARACTERES_ESPECIALES:
            cont_especiales += 1
        elif contrasenia[indice].isnumeric():
            cont_num += 1
        elif contrasenia[indice].islower():
            cont_minus += 1
        elif contrasenia[indice].isupper():
            cont_mayus += 1
        else:
            validacion= False
        indice += 1
    validacion= cont_mayus >= int(CONFIGURACION['CONTEO_MINIMO']) and cont_minus >= int(CONFIGURACION['CONTEO_MINIMO']) and cont_num >= int(CONFIGURACION['CONTEO_MINIMO']) and cont_especiales >= int(CONFIGURACION['CONTEO_MINIMO']) and int(CONFIGURACION['MIN_LONG_CONTRASEniA']) <= len(contrasenia) and len(contrasenia) <= int(CONFIGURACION['MAX_LONG_CONTRASEniA']) 
    return validacion
    
def iniciar_sesion(usuario, contrasenia, nombre_usuario_entry, contrasenia_entry, raiz):
    # Hecha por Luciano Vicini
    """
    * Esta funcion se encarga de revisar si el usuario y contrasenia ingresados corresponden
    *   a un usuario ya registrado
    *
    * Pre: recibe 2 cadenas de caracteres correspondientes al usuario y a la contrasenia
    *
    * Post: devuelve una variable resultado con mensajes de error en caso de no haber sido 
    *   correctos los datos ingresados o con la modificacion en la lista de usuarios participantes
    *   en caso de encontrarse registrado
    """
    with open('usuarios.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        cont = 0
        for fila in lector:
            if fila[int(CONFIGURACION['USUARIO'])] == usuario:
                if fila[int(CONFIGURACION['CONTRASENIA'])] == contrasenia:
                    cont = -1
                    resultado = usuarios_participantes(usuario, jugadores)
                    
                    nombre_usuario_entry.delete(0,len(usuario))
                    contrasenia_entry.delete(0,len(contrasenia))
                    if len(jugadores) == 4:
                        raiz.destroy()
                else:
                    cont = 1
        if cont == 1:
            resultado = messagebox.showerror(message='contrasenia incorrecta')
        elif cont == 0:
            resultado = messagebox.showerror(message='este usuario no esta registrado')
    return resultado

#con esta funcion te registras
def registrarse():
    Registro= Tk()
    
    def registro(usuario,contrasenia):
        #este with open es para comprobar si ya esta registrado ese usuario
        with open('usuarios.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            cont= 0
            for fila in lector:
                if fila[int(CONFIGURACION['USUARIO'])] == usuario:
                    cont += 1
        if cont == 0:
            if validar_usuario(usuario) and validar_contrasenia(contrasenia):
                with open('usuarios.csv','a',newline='\n') as archivo:
                    escritor = csv.writer(archivo)
                    escritor.writerow([usuario,contrasenia])
                    messagebox.showinfo(message= 'has sido registrado exitosamente')
                    Registro.destroy()
            else:
                messagebox.showerror(message= '''Ingrese un nombre de usuario o contrasenia validos    (NOMBRE DE USUARIO entre 4 y 20 caracteres con -, letras, numeros)   (CONTRASEniA: longitud entre 6 y 12 caracteres, por lo menos 1 mayus,minus,numero y alguno de los siguientes elementos: #, !)''')
                
        else:
            messagebox.showerror(message= 'este usuario ya esta registrado') 
            
    Registro.config(background='lightyellow',width='400',height='180')
    Registro.title('Registro de Usuario')
    
    R_nombre_usuario_entry= Entry(Registro)
    R_nombre_usuario_entry.place(x= 200, y=40)
    R_contrasenia_entry= Entry(Registro)
    R_contrasenia_entry.place(x=200, y= 80)
    R_contrasenia_entry.config(show= '*')

    R_nombre_usuario_label= Label(Registro, text= 'Nombre de Usuario:', bg='lightyellow')
    R_nombre_usuario_label.place(x=70, y=40)
    R_contrasenia_label= Label(Registro, text= 'contrasenia:', bg='lightyellow')
    R_contrasenia_label.place(x=115, y= 80)
    
    R_registrarse_boton= Button(Registro,text= 'Registrarse',command= lambda:registro(R_nombre_usuario_entry.get(),R_contrasenia_entry.get()))
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
    contrasenia_label= Label(raiz, text= 'contrasenia:', bg='lightblue')
    contrasenia_label.place(x=115, y= 80)

    iniciar_partida_boton= Button(raiz,text='     Iniciar Partida     ',command= lambda: iniciar_partida())
    iniciar_partida_boton.place(x=133, y= 220)
    iniciar_sesion_boton= Button(raiz,text='Iniciar Sesion',command= lambda: iniciar_sesion(nombre_usuario_entry.get(), contrasenia_entry.get(), nombre_usuario_entry, contrasenia_entry, raiz))
    iniciar_sesion_boton.place(x=150, y= 120)
    registrarse_txt= Label(raiz, text= 'si no tenes cuenta presiona en el boton de abajo', bg='lightblue', fg= 'blue')
    registrarse_txt.place(x=60, y= 150)
    registrarse_boton= Button(raiz,text= 'Registrarse',command= lambda: registrarse())
    registrarse_boton.place(x=156, y=180)

    raiz.mainloop()
    return jugadores
