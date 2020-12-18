"""
Crear un programa con:
-Ventana
-Tamaño fijo
-No redimensionable
-Un menu
-Diferentes patanllas
-Formulario de añadit productos
-Guardar datos temporales
-Mostrar datos listados en la pantalla de home para
-Opcion de salir
"""

from tkinter import *

#Definir ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto Tkinter")
ventana.resizable(0,0)

#Pantallas
def home():
    #Mostrar pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)

    #Ocultar pantalla

    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add():
    #Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=130,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    #Campos del formulario
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5,sticky=W)

    #Ocultar pantalla

    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=150,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    #Ocultar pantalla

    add_label.grid_remove()
    home_label.grid_remove()

    return True

#Variables importantes
name_data = StringVar()
price_data = StringVar()

#Definir campos de pantalla Inicio
home_label = Label(ventana, text="Inicio")

#Definir campos de pantalla add
add_label = Label(ventana, text="Añadir producto")

#Campos del formulario
add_name_label= Label(ventana, text="Nombre: ")
add_name_entry= Entry(ventana, textvariable=name_data)

add_price_label= Label(ventana, text="Precio: ")
add_price_entry= Entry(ventana, textvariable=price_data)

add_descipcion_label= Label(ventana, textvariable="Descripcion: ")
add_price_entry= Text(ventana)

#Definir campos de pantalla Info
info_label = Label(ventana, text="Informacion")
data_label =Label(ventana, text="Creado por Alex . 2020")

#Cargar pantalla inicio
home()

#Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#Cargar menu
ventana.config(menu=menu_superior)

#Cargar ventana
ventana.mainloop()