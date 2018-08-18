import sqlite3
from PyQt5.QtWidgets import QMessageBox, QWidget
from setting_GUI.database.run_datebase import Database


def crear_sesion(usuario: str, apellidos: str, edad: int, email: str, password: str):
        noproblema = Database().crear(usuario, apellidos, edad, email, password)
        if noproblema:
            QMessageBox.information(QWidget(), "Milnes", "Su Cuenta ha sido registrada: {}".format(email))
            return True
        else:
            return False

