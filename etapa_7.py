from tkinter import *
from tkinter import messagebox
import csv
raiz= Tk()

#CONSTANTES
USUARIO= 0
CONTRASEÑA= 1
MIN_LONG_USUARIO= 4
MAX_LONG_USUARIO= 20
MIN_LONG_CONTRASEÑA= 6
MAX_LONG_CONTRASEÑA= 12
CONTEO_MINIMO= 1
CARACTERES_ESPECIALES= ['#','!']

#Esta es la lista de usuarios que van a jugar
jugadores= []

#esta funcion agrega a la lista de jugadores los nombres de los usuarios a participar
def usuarios_participantes(usuario,contraseña):
    if usuario in jugadores:
        messagebox.showerror(message='Este jugador ya esta participando')
    else:
        jugadores.append(usuario)
        messagebox.showinfo(message=f'{usuario} participará del juego')
    nombre_usuario_entry.delete(0,len(usuario))
    contraseña_entry.delete(0,len(contraseña))
    if len(jugadores) == 4:
        raiz.destroy()
        
#esta funcion hace que se cierre el programa pero mantengas la lista de jugadores
def iniciar_partida():
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
    return validacion and MIN_LONG_USUARIO <= len(usuario) and len(usuario) <= MAX_LONG_USUARIO

#esta funcion comprueba si la contraseña del usuario es valido cuando se registra el jugador
def validar_contraseña(contraseña):
    cont_especiales= 0
    cont_num = 0
    cont_minus = 0
    cont_mayus = 0
    indice = 0
    validacion= True
    while indice < len(contraseña) and validacion==True:
        if contraseña[indice] in CARACTERES_ESPECIALES:
            cont_especiales += 1
        elif contraseña[indice].isnumeric():
            cont_num += 1
        elif contraseña[indice].islower():
            cont_minus += 1
        elif contraseña[indice].isupper():
            cont_mayus += 1
        else:
            validacion= False
        indice += 1
    validacion= cont_mayus >= CONTEO_MINIMO and cont_minus >= CONTEO_MINIMO and cont_num >= CONTEO_MINIMO and cont_especiales >= CONTEO_MINIMO and MIN_LONG_CONTRASEÑA <= len(contraseña) and len(contraseña) <= MAX_LONG_CONTRASEÑA 
    return validacion

#esta funcion inicia sesion
def iniciar_sesion(usuario, contraseña):
    with open('usuarios.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        cont = 0
        for fila in lector:
            if fila[USUARIO] == usuario:
                if fila[CONTRASEÑA] == contraseña:
                    cont = -1
                    resultado= usuarios_participantes(fila[0],fila[1])
                else:
                    cont += 1
        if cont == 1:
            resultado= messagebox.showerror(message='contraseña incorrecta')
        elif cont == 0:
            resultado= messagebox.showerror(message='este usuario no esta registrado')
    return resultado

#con esta funcion te registras
def registrarse():
    Registro= Tk()
    
    def registro(usuario,contraseña):
        #este with open es para comprobar si ya esta registrado ese usuario
        with open('usuarios.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            cont= 0
            for fila in lector:
                if fila [USUARIO] == usuario:
                    cont += 1
        if cont == 0:
            if validar_usuario(usuario) and validar_contraseña(contraseña):
                with open('usuarios.csv','a',newline='\n') as archivo:
                    escritor = csv.writer(archivo)
                    escritor.writerow([usuario,contraseña])
                    messagebox.showinfo(message= 'has sido registrado exitosamente')
                    Registro.destroy()
            else:
                messagebox.showerror(message= '''Ingrese un nombre de usuario o contraseña validos    (NOMBRE DE USUARIO entre 4 y 20 caracteres con -, letras, numeros)   (CONTRASEÑA: longitud entre 6 y 12 caracteres, por lo menos 1 mayus,minus,numero y alguno de los siguientes elementos: #, !)''')
                
        else:
            messagebox.showerror(message= 'este usuario ya esta registrado') 
            
    Registro.config(background='lightyellow',width='400',height='180')
    Registro.title('Registro de Usuario')
    
    R_nombre_usuario_entry= Entry(Registro)
    R_nombre_usuario_entry.place(x= 200, y=40)
    R_contraseña_entry= Entry(Registro)
    R_contraseña_entry.place(x=200, y= 80)
    R_contraseña_entry.config(show= '*')

    R_nombre_usuario_label= Label(Registro, text= 'Nombre de Usuario:', bg='lightyellow')
    R_nombre_usuario_label.place(x=70, y=40)
    R_contraseña_label= Label(Registro, text= 'contraseña:', bg='lightyellow')
    R_contraseña_label.place(x=115, y= 80)
    
    R_registrarse_boton= Button(Registro,text= 'Registrarse',command= lambda:registro(R_nombre_usuario_entry.get(),R_contraseña_entry.get()))
    R_registrarse_boton.place(x=150, y= 120)
    
    Registro.mainloop()

raiz.config(background='lightblue',width='400',height='250')
raiz.title('Ingreso de Usuarios')
raiz.resizable(0,0)

nombre_usuario_entry= Entry(raiz)
nombre_usuario_entry.place(x= 200, y=40)
contraseña_entry= Entry(raiz)
contraseña_entry.place(x=200, y= 80)
contraseña_entry.config(show= '*')

nombre_usuario_label= Label(raiz, text= 'Nombre de Usuario:', bg='lightblue')
nombre_usuario_label.place(x=70, y=40)
contraseña_label= Label(raiz, text= 'contraseña:', bg='lightblue')
contraseña_label.place(x=115, y= 80)

iniciar_partida_boton= Button(raiz,text='     Iniciar Partida     ',command= lambda: iniciar_partida())
iniciar_partida_boton.place(x=133, y= 220)
iniciar_sesion_boton= Button(raiz,text='Iniciar Sesion',command= lambda: iniciar_sesion(nombre_usuario_entry.get(), contraseña_entry.get()))
iniciar_sesion_boton.place(x=150, y= 120)
registrarse_txt= Label(raiz, text= 'si no tenes cuenta presiona en el boton de abajo', bg='lightblue', fg= 'blue')
registrarse_txt.place(x=60, y= 150)
registrarse_boton= Button(raiz,text= 'Registrarse',command= lambda: registrarse())
registrarse_boton.place(x=156, y=180)

raiz.mainloop()