print("----------Ejemplo 1--------")

nombre = "Alexander Correa"

print(nombre)
print(type(nombre)) #Tipo de variable

print("----------Ejemplo 2--------")

comprobar = isinstance(nombre, str) #Tipo de variable
if comprobar:
    print("Esa variable es un String")

else:
    print("no es una cadena")

if not isinstance(nombre, float):
    print("La variable no es flotante")

print("----------Ejemplo 3--------")

#limpiar espacios

frase = ("    mi contenido     ")

print(frase)
print(frase.strip())

print("----------Ejemplo 4--------")

#Eliminar variable

year = 2020

print(year)
del year

print("----------Ejemplo 5--------")

#Comprobar variable vacia

texto = "   ff   "

if len(texto) <= 0:
    print("La variable esta vacia")

else:
    print("La variable no esta vacia ",len(texto))

print("----------Ejemplo 6--------")

#encontrar caracteres
frase = ("La vida es bella")
print(frase.find("vida"))

print("----------Ejemplo 7--------")

#remplazar palabras en un string

new_frase = frase.replace("vida", "moto")
print(new_frase)

