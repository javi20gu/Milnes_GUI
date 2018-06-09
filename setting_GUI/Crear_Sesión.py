import sqlite3
from PyQt5.QtWidgets import QMessageBox, QWidget


def crear_sesion(usuario: str, apellidos: str, edad: int, email: str, password: str):
    conexion = sqlite3.connect("login.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO login (usuario, apellidos, edad, email, password) "
                       "VALUES('{}', '{}','{}','{}','{}')".format(usuario, apellidos,
                                                                  edad, email, password))

        QMessageBox.information(QWidget(), "Milnes", f"Su Cuenta ha sido registrada: {email}")
        conexion.commit()
        conexion.close()
        return True

    except sqlite3.IntegrityError:
        QMessageBox.warning(QWidget(), "Milnes", f"Email ya existente: {email}")
        conexion.commit()
        conexion.close()
        return False
