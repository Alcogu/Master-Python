from tkinter import *
import os.path

class Programa:

    def __init__(self):

        self.title = "Master en Python"
        self.icon = "./Imagenes/Logo.ico"
        self.icon_alt = "./21-Tkinder/Imagenes/Logo.ico" #Icono alternativo
        self.size = "770x740"
        self.resizable = FALSE

    def cargar(self):
        #Crear ventana raiz
        ventana = Tk()
        self.ventana = ventana

        #Titulo de la venta
        ventana.title(self.title)

        #Comprobar si hay un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        #Icono de la venta
        ventana.iconbitmap(ruta_icono)

        #Mostrar texto en el progra
        texto = Label(ventana, text = ruta_icono)
        texto.pack()

        #Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        #Bloquear el tamaño de la venta
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(1, 1)

    def addTexto(self):
        texto = Label(self.ventana, text="Hola desde un Metodo")
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

#instanciar programa
programa = Programa()
programa.cargar()
programa.addTexto()
programa.mostrar()