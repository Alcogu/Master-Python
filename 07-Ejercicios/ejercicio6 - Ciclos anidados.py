"""
Mostrar las tablas del 1 al 10 mostrando sus titulos
"""

for cabecera in range (1, 11):
    print("----------------------")
    print(f"-----Tabla del {cabecera}-----")
    print("----------------------")

    for numero in range (1, 11):
        print(f"{cabecera} x {numero} = {cabecera * numero}")
    print("\n")