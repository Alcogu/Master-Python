import Usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nVamos a registrarte")

        nombre = input("Ingresa tu nombre: ")
        apellidos = input("Ingresa tus apellidos: ")
        email = input("Registra tu email:")
        password = input("Registra tu contraseña:")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >=1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")

        else:
            print("no te has registrado correctamente")

    def login(self):
        print("\nIdentificate")

        email = input("Ingresa tu email:")
        password = input("Ingresa tu contraseña:")