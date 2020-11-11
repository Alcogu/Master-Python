from io import open
import pathlib
import shutil #acceder a fuciones de copiar y renombrar archivos

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

#contenido = archivo_lectura.read()
#print(contenido)

#Leer contenido y guardarlo en lista

lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:

    lista_frase = frase.split()
    print(lista_frase)
    #print("- " + frase.upper())

#copiar
"""
ruta_original = str(pathlib.Path().absolute()) + "/ficheros.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = "../07-ejercicios/ficheros_copiado77.txt"

shutil.copyfile(ruta_original, ruta_alternativa)
"""
#Mover

ruta_original = str(pathlib.Path().absolute()) + "/ficheros_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/ficheros_NewCopy.txt"

shutil.move(ruta_original, ruta_nueva)