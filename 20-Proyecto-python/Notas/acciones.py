import Notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nListo {usuario[1]} vamos a crear una nueva nota")
        
        titulo = input("Ingresa el titulo de la nota: ")
        descripcion = input("Escribe el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nSe ha guardado la nota: {nota.titulo}")

        else:
            print(f"\nNo se ha guardado la nota {usuario[1]}")

    def mostrar (self, usuario):
        print(f"\nListo {usuario[1]}!! aquí tienes tus notas")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n------------------------------------")
            print(nota[2])
            print(nota[3])
            print("\n------------------------------------")

    def borrar(self, usuario):
        print(f"\nListo {usuario[1]} vamos a borrar notas")

        titulo = input("Ingresa el titulo de la nota que se borrará ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar [0] >= 1:
            print(f"Se ha eliminado la nota: {nota.titulo} ")

        else:
            print("No se a borrado la nota ")