from tkinter import *

ventana = Tk()
#ventana.geometry("700x500")

texto = Label(ventana, text = "Hola que Hola")

texto.config(
    fg="white",
    bg="black",
    padx=20,
    pady=20,
    font=("Consola", 30)
    )
texto.pack(side=TOP)

texto = Label(ventana, text = "Callate Flanders")
texto.config(
    height=3,
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=TOP, fill=X, expand=YES)# se cambia anchor por side

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
texto.pack(side=LEFT)

texto = Label(ventana, text = pruebas(nombre = "Osita", apellidos = "Correa Maria", pais = "Colombia"))
texto.config(
    height=3,
    bg="Green",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT)

ventana.mainloop()