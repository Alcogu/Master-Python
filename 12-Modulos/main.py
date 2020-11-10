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

print(holaMundo("Peluchito"))