import clases

persona = clases.Persona()
persona.setNombre("Alexander")
persona.setApellidos("Correa Gutiérrez")
persona.setAltura("175cm")
persona.setEdad("27")

#print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())