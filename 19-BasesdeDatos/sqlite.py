import sqlite3 #importar modulo

#Conexion
conexion = sqlite3.connect("pruebas.db")

#Crear cursor
cursor = conexion.cursor()

#crear una tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT not null, "+
"titulo VARCHAR(255), "+
"description TEXT, "+
"precio int(255)"+
")")

#Guardar Cambios
conexion.commit()

#Cerrar conexion
conexion.close()