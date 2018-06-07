import sqlite3

conexion = sqlite3.connect("login.db")
cursor = conexion.cursor()
try:
    cursor.execute("CREATE TABLE login(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Edad INTEGER NOT NULL, Usuario "
                   "VARCHAR(15) NOT NULL, Apellidos VARCHAR(50) NOT NULL, Email VARCHAR(60) UNIQUE NOT NULL, Password "
                   "varchar(90) NOT NULL)")

except sqlite3.OperationalError as a:
    print("---------Tabla ya Creada---------")

conexion.commit()
conexion.close()
