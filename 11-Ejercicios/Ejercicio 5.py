"""
Crear una lista con el contenido de esta tabla:
video juegos de: 
Accion  Aventura            Deportes

GTA     Assasins            Fifa 21
cod     Crash               Pro21
pubg    Prince of persia    Moto GP

Mostrar información ordenada
"""

tabla = [ #Listas dentro de los diccionarios dentro de la lista
    {
        "categoria": "-Accion-",
        "Juegos": ["GTA", "call of duty", "PUGb"]
    },
    {
        "categoria": "Aventura",
        "Juegos": ["Assasins", "Crash", "Prince of Persia"]
    },
    {
        "categoria": "Deportes",
        "Juegos": ["Fifa 21", "Pes 21", "Moto GP 21"]
    }
]

for categoria in tabla:
    print(f"-------------------{categoria['categoria']}-------------------")

    for juego in categoria['Juegos']:
        print(juego)