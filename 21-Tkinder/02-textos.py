from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text = "Hola que Hola")

texto.config(
    fg="white",
    bg="black",
    padx=20,
    pady=20,
    font=("Consola", 30)
    )
texto.pack()

texto = Label(ventana, text = "Callate Flanders")
texto.config(
    height=3,
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(anchor=E)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais} "

texto = Label(ventana, text = pruebas(nombre = "Alexander", apellidos = "Correa Gutiérrez", pais = "Colombia"))
texto.config(
    height=3,
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(anchor=NW)

ventana.mainloop()