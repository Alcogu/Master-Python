"""
Comprobar que una variable esta vacia y si lo esta rellenarla 
con texto en minusulas y pasarla a mayusculas
"""

variable = ""

if len(variable.strip()) <= 0:

    variable = "Texto prueba"
    print(variable.upper())

else:
    print(f"la variable tiene contenido {variable}")
