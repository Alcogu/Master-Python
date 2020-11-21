import sqlite3 #importar modulo

#Conexion
conexion = sqlite3.connect("pruebas.db")

#Crear cursor
cursor = conexion.cursor()

#crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT not null, 
titulo VARCHAR(255), 
description TEXT, 
precio int(255)
);""")

#Guardar Cambios
conexion.commit()#Se guardan cambios

#insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'producto uno', 'descripcion del producto', '550')")
conexion.commit()#Se guardan cambios

#Borrar Datos
cursor.execute("DELETE FROM productos")#Borra todo
conexion.commit()

#Insertar datos
productos =[
    ("Portatil", "aguanta", 1500000),
    ("Celular", "suave", 200000),
    ("Anillo", "melo", 250000),
    ("condones", "los del tino", 20000),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)", productos)#Varias consultas de una
conexion.commit()#Ejecuta lo de arriba

#Listar Datos
#cursor.execute("SELECT * FROM productos;")
cursor.execute("SELECT * FROM productos WHERE precio >=1000000;")
productos = cursor.fetchall()

#print(cursor)#Ver obejto que se tiene dentro de cursor
#print(productos)#Muestra listas con objetos asignados

for producto in productos:#imprime cada producto
    #print(producto)
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Nombre: ", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")

producto = cursor.fetchone()#primero producto
print(producto)

#Cerrar conexion
conexion.close()