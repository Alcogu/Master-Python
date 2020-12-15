from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=100)

def sacarAlerta():
    #MessageBox.showinfo("Alerta", "deja de darle ahí")
    #MessageBox.showerror("Alerta", "deja de darle ahí")
    MessageBox.showwarning("Alerta", "deja de darle ahí")

Button(ventana, text="Mostar Alerta", command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Alerta", "¿quieres continuar?")

    if resultado != "no":
        MessageBox.showinfo("Chao", f"Adios {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("Alex")).pack()

ventana.mainloop()