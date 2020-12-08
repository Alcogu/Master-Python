"""
Tkinder es un modulo para crear interfaces grafcas
"""

from tkinter import *

#Crear ventana raiz
ventana = Tk()

#Titulo de la venta
ventana.title("Interfaz Gráfica con Alexiño")

#Icono de la venta
ventana.iconbitmap("./21-tkinder/Imagenes/logo.ico")

#Cambio en el tamaño de la ventana
ventana.geometry("750x450")

#Bloquear el tamaño de la venta
ventana.resizable(0, 0)

# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()