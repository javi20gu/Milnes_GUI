import sqlite3
from PyQt5.QtWidgets import QWidget, QMessageBox


class Sql:

    @classmethod
    def query(cls, *args: str):
        conexion = sqlite3.connect("login.db", timeout=10*1000)
        cursor = conexion.cursor()
        cursor.execute(*args)
        conexion.commit()

        return cursor


class Database:

    @classmethod
    def create(cls):
        Sql.query("CREATE TABLE login(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Edad INTEGER NOT NULL, Usuario "
                  "VARCHAR(15) NOT NULL, Apellidos VARCHAR(50) NOT NULL, Email VARCHAR(60) UNIQUE NOT NULL, Password "
                  "varchar(90) NOT NULL)")

    @classmethod
    def usuarios(cls) -> list:
        cursor = Sql.query("SELECT Email, Password FROM login")
        usuarios = cursor.fetchmany(-1)

        return usuarios

    @classmethod
    def buscar_por_email(cls, email: str):
        cursor = Sql.query("SELECT * FROM login WHERE Email='{}'".format(email))
        usuario = cursor.fetchone()

        return usuario

    @classmethod
    def cambiar_edad(cls, antigua_edad: int, nueva_edad: int):
        Sql.query("UPDATE login SET Edad=? Where Edad=? ", (nueva_edad, antigua_edad))

    @classmethod
    def cambiar_apellidos(cls, antigua_apellido: str, nuevo_apellidos: str):
        Sql.query("UPDATE login SET Apellidos=? Where Apellidos=? ", (nuevo_apellidos, antigua_apellido))

    @classmethod
    def cambiar_password(cls, antigua_password: str, nuevo_password: str):
        Sql.query("UPDATE login SET Password=? Where Password=? ", (nuevo_password, antigua_password))

    @classmethod
    def cambiar_usuario(cls, antiguo_usuario: str, nuevo_usuario: str):
        Sql.query("UPDATE login SET Usuario=? WHERE Usuario=? ", (nuevo_usuario, antiguo_usuario))

    @classmethod
    def cambiar_email(cls, antiguo_email: str, nuevo_email: str):
        try:
            Sql.query("UPDATE login SET Email=? Where Email=? ", (nuevo_email, antiguo_email))
            return True
        except sqlite3.IntegrityError as a:
            QMessageBox.warning(QWidget(), "Milnes", f"Email ya existente: {nuevo_email}")
            return False
    @classmethod
    def eliminar_cuenta(cls, email: str):
        Sql.query("DELETE FROM login WHERE Email=:email", {"email": email})

    def crear(self, usuario: str, apellidos: str, edad: int, email: str, password: str):
        try:
            Sql.query("INSERT INTO login (usuario, apellidos, edad, email, password) "
                  "VALUES('{}', '{}','{}','{}','{}')".format(usuario, apellidos,
                                                             edad, email, password))
            return True
        except sqlite3.IntegrityError:
            QMessageBox.warning(QWidget(), "Milnes", f"Email ya existente: {email}")
            return False