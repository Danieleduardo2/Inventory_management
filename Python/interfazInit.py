from tkinter import *
from Ferreteria.Python.funcionalidades import Funcionalidades  # Importar la clase Funcionalidades
from menuPrincipal import *

# Crear una instancia de la clase Funcionalidades
funciones = Funcionalidades()

def intentar_iniciar_sesion():
    usuario = ingresarUsuario.get()
    contraseña = ingresarContraseña.get()
    if funciones.iniciar_sesion(usuario, contraseña):
       if(usuario == 'admin'):
        root.destroy()  # Cierra la ventana actual
        screen2()
       else:
        root.destroy()  
        screen3()
    else:
        resultado.config(text="Usuario o contraseña incorrectos", fg="red")

root = Tk()
root.title("Ferreteria huerto de riego")
root.geometry("1300x700")

label_imagen = Label(root, image="")
label_imagen.place(relwidth=1, relheight=1)

fuente = ('Arial', 10, 'bold') 

mensajeIngresarU = Label(root, text="INGRESE SU USUARIO", bg="orange", font=fuente)
mensajeIngresarU.place(x=560, y=240)
ingresarUsuario = Entry(root, width=30)
ingresarUsuario.place(x=550, y=280)

mensajeIngresarC = Label(root, text="INGRESE SU CONTRASEÑA", bg="orange", font=fuente)
mensajeIngresarC.place(x=550, y=370)
ingresarContraseña = Entry(root, width=30, show='*')
ingresarContraseña.place(x=550, y=400)

iniciarSesion = Button(root, text="Iniciar Sesión", command=intentar_iniciar_sesion, bg="white")
iniciarSesion.place(x=600, y=450)

resultado = Label(root, text="", font=fuente)
resultado.place(x=560, y=500)




root.mainloop()
