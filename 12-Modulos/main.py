"""
Son funcionalidades ya hechas para reutilizar.
"""
#Importar modulo propio

#primera forma
"""
import mimodulo

print(mimodulo.holaMundo("Peluchito"))
print(mimodulo.calculadora(3,5, True))
"""
#Segunda Forma

#from mimodulo import *  importa todo
from mimodulo import holaMundo

#print(holaMundo("Peluchito"))

# Modulo Fechas

import datetime

#print(datetime.date.today())

fechacompleta = datetime.datetime.now()
"""
print(fechacompleta)
print(fechacompleta.year)
print(fechacompleta.day)
print(fechacompleta.month)
"""
fechapersonalizada = fechacompleta.strftime("%d/%m/%Y, ")
#print("Mi fecha personalizada", fechapersonalizada)

#Modulo Matematicas

import math

print("Pi es: ", math.pi)
print("Raiz cuadrada de 10: ", math.sqrt(5))
print("Redondear: ", math.floor(6.1545521))
print("Redondear: ", math.ceil(6.1545521))

import random

print("Número aleatorio entre 50 a 100 = ", random.randint(50, 100))