"""
Proyecto Python mysq:
-Abrir asistente-Login o registro
-opciones varias
"""
from Usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")

hazEL = acciones.Acciones()#Crea el objeto o instancia la clase


accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
    hazEL.registro()

elif accion == "login":
    hazEL.login()