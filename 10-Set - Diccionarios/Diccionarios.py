"""
Diccionario: TIpo de dato que almacena un conjunto de datos.
En formato clave > valor
Es parecido a un array asociativo o un objeto json
"""

persona = {
    "nombre" : "Alexander",
    "apellidos" : "Correa Gutiérrez",
    "web" : "alexweb.com"
}

#print(persona)
#print(persona["web"])

#Lista con diccionarios

contactos =[
    {
        "nombre": "Alexander",
        "email" : "alex@msn.com"
    },
    {
        "nombre": "Osita",
        "email" : "osita@msn.com"
    },
    {
        "nombre": "Kathe",
        "email" : "peluchito@msn.com"
    }
]

contactos[0]["nombre"] = "Alexito"
#print(contactos[0]["nombre"])

print("\nListado de contactos: ")

for contacto in contactos:
    print(f"\nNombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("--------------------------------------------")