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
conexion.commit()#Se guardan cambios

#insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'producto uno', 'descripcion del producto', '550')")
conexion.commit()#Se guardan cambios

#Listar Datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

#print(cursor)#Ver obejto que se tiene dentro de cursor
print(productos)#Muestra listas con objetos asignados

#Cerrar conexion
conexion.close()