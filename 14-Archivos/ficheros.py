from io import open
import pathlib

ruta = str(pathlib.Path().absolute()) + "/ficheros.txt"
archivo = open (ruta, "a+")

#Escribir

archivo.write("*************** Soy un texto metido desde Python***************\n")

#Cerrar archivo
archivo.close()

# Abrir Archivo
ruta = str(pathlib.Path().absolute()) + "/ficheros.txt"
archivo_lectura = open (ruta, "r+")

#Leer contenido

contenido = archivo_lectura.read()

for elemento in contenido:
    print(elemento)