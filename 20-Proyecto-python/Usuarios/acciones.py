import Usuarios.usuario as modelo
import Notas.acciones

class Acciones:

    def registro(self):
        print("\nVamos a registrarte")

        nombre = input("Ingresa tu nombre: ")
        apellidos = input("Ingresa tus apellidos: ")
        email = input("Registra tu email: ")
        password = input("Registra tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >=1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")

        else:
            print("\nno te has registrado correctamente")

    def login(self):
        print("\nIdentificate")

        try:
            email = input("Ingresa tu email: ")
            password = input("Ingresa tu contraseña: ")

            usuario = modelo.Usuario("", "", email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenid@ {login[1]}, te has registrado en el sistema el {login[5]} ")
                self.nextAction(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"El Login es incorrecto")

    def nextAction(self, usuario):
        print("""
        Acciones disponibles:
        - Crear Nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir
        """)

        accion = input("¿qué quieres hacer? ")
        #se llama modulo de acciones y a la clase Acciones para crear el objeto
        hazEl = Notas.acciones.Acciones()
        
        if accion == "crear":
            hazEl.crear(usuario)
            self.nextAction(usuario)

        elif accion == "mostrar":
            print("Vamos a mostrar una nota")
            self.nextAction(usuario)

        elif accion == "eliminar":
            print("Vamos a eliminar una nota")
            self.nextAction(usuario)

        elif accion == "Salir":
            print(f"¡¡¡Hasta la vista viejo!!!")
            exit()