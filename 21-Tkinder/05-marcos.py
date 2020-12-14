from tkinter import *

ventana = Tk()
ventana.title("Marcos")
ventana. geometry("700x700")

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="red", 
    bd=5, 
    relief="solid"
)
marco.pack(side=LEFT, anchor=NW)
marco.pack_propagate(False)

texto = Label(marco, text="Primer Marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20),
    bd=3,
    relief=SOLID,
    anchor=CENTER
)
texto.pack(fill=Y, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="green", 
    bd=5, 
    relief="solid"
)
marco.pack(side=RIGHT, anchor=NE)

marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="yellow", 
    bd=12, 
    relief="solid"
)

marco.pack(side=LEFT, anchor=SE)

marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="blue", 
    bd=12, 
    relief="solid"
)

marco.pack(side=RIGHT, anchor=SW)

ventana.mainloop()