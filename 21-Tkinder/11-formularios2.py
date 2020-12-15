from tkinter import *

ventana = Tk()
ventana.geometry("800x300")

encabezado = Label(ventana, text = "Formulario #2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)
encabezado.pack(anchor=N,side=TOP, fill=X, expand=YES)

#Botones Check

#Radio button

#Menu de opciones

ventana.mainloop()