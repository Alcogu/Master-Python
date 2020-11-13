import clases

persona = clases.Persona()
persona.setNombre("Alexander")
persona.setApellidos("Correa Gutiérrez")
persona.setAltura("175cm")
persona.setEdad("27")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("----------------------------------")

informatico = clases.Informatico()
informatico.setNombre("Alexander")
informatico.setApellidos("Correa Gutiérrez")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(f"Los lenguajes que sabe son: {informatico.getLenguajes()}")
print(informatico.caminar())
print(informatico.experiencia)

print("----------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes, tecnico.getNombre())