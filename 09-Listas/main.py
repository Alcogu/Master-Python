"""
Listas: colecciones o conjuntos de datos bajo un unico nombre
para acceder a ess valores podemos usar un indice numerico
"""
"""
pelicula = "Batman"

#Definir lista
peliculas = ["Spiderman", "Lord of the Ring", "Harry Potter"]
cantantes = list(("pepito perez" , "Juanito", "pepito"))
years = list(range(2020, 2050))

print(peliculas)
print(cantantes)
print(years)

#Indices

print(peliculas[0])
print(cantantes[0:2])
print(peliculas[1:])

#añadir elementos a lista

cantantes.append("Juanes")
print(cantantes)

#Recorrer lista
print("\n----------LISTADO PELICULAS---------")

nueva_pelicula =""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Ingresa la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

#Listas multidimensionales
"""
print("\n**********Contactos************")

contactos = [
    [
        "Alexander",
        "alex@men.com"
    ],
    [
        "Kathe",
        "amorcito@mia.com"
    ]
]

for contacto in contactos:
    for elemento in contacto:
        print(elemento)
    print("\n")
#print(contactos)