from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text = "GenJutsu from Itachi").pack(anchor=W)

imagen = Image.open("./21-Tkinder/Imagenes/Itachi.jpg")
render = ImageTk.PhotoImage(imagen)

Label(ventana, image = render).pack()

ventana.mainloop()