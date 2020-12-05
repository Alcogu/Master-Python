import Notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nListo {usuario[1]} vamos a crear una nueva nota")
        
        titulo = input("Ingresa el titulo de la nota: ")
        descripcion = input("Escribe el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nSe ha guardado la nota: {nota.titulo} ")

        else:
            print(f"\nNo se ha guardado la nota {usuario[1]} ")