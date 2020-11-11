from io import open
import pathlib

# Abrir Archivo
ruta = str(pathlib.Path().absolute()) + "/ficheros.txt"
archivo = open (ruta, "a+")