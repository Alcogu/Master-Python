"""
Pedir la nota de cualquier cantidad de alumnos y sacar por pantalla cuantos han aprobado y cuantos no
"""

contador = 1
aprobados = 0
suspendidos = 0

n_alumnos = int(input("¿cuantos alumnos tiene?"))

while contador <= n_alumnos:
    nota = int(input(f"¿Qué nota obtuvo al \alumno {contador}?"))

    if nota >= 3:
        aprobados +=1

    else:
        suspendidos += 1

    contador += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")