import sqlite3
from PyQt5.QtWidgets import QMessageBox
from run import Widgets


def crear_sesion(usuario: str, apellidos: str, edad: int, email: str, password: str):
    conexion = sqlite3.connect("login.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO login (usuario, apellidos, edad, email, password) "
                       "VALUES('{}', '{}','{}','{}','{}')".format(usuario, apellidos,
                                                                  edad, email, password))

        QMessageBox.information(Widgets(), "Milnes", f"Su Cuenta ha sido registrada: {email}")
        conexion.commit()
        conexion.close()
        return True

    except sqlite3.IntegrityError:
        QMessageBox.warning(Widgets(), "Milnes", f"Email ya existente: {email}")
        conexion.commit()
        conexion.close()
        return False
