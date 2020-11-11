#Gestion de carpetas
import shutil
import os

#crear carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("ya existe")

#Eliminar carpeta

#os.rmdir("./mi_carpeta")

#Copiar una carpeta
"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"

shutil.copytree(ruta_original, ruta_nueva)
"""
#Se elimina carpeda copiada
"""
os.rmdir("./mi_carpeta_COPIADA")
"""

print("Contenido de la carpeta")
contenido = os.listdir("./mi_carpeta")
#print(contenido) contenido de la carpeta

for fichero in contenido:
    print("fichero: " + fichero)