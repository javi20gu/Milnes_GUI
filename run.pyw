import sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QInputDialog
from PyQt5.QtGui import QPixmap, QIcon
from sys import exit, argv, path
from subprocess import call
from pathlib import Path
from setting_GUI import *
from os import getcwd

class Inicio(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_3 = Ui_Inicio()
        self.ui_3.setupUi(self)
        self.ui_3.botonEmail.clicked.connect(self.cambiarEmail)
        self.ui_3.botonEmail_2.clicked.connect(self.cambiarPassword)
        self.ui_3.botonEmail_3.clicked.connect(self.cambiarUsuario)
        self.ui_3.botonEmail_5.clicked.connect(self.cambiarApellidos)
        self.ui_3.botonEmail_6.clicked.connect(self.cambiarEdad)
        self.ui_3.pushButton_2.clicked.connect(self.cerrarSesion)
        self.ui_3.pushButton.clicked.connect(self.eliminarCuenta)
        self.ui_3.flecha1.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/flecha.png"))
        self.ui_3.flecha2.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/flecha.png"))
        self.ui_3.flecha3.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/flecha.png"))
        self.ui_3.flecha4.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/flecha.png"))
        self.ui_3.flecha5.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/flecha.png"))
        self.ui_3.pushButton.setIcon(QIcon(f"{getcwd()}/setting_GUI/borrar.png"))
        self.ui_3.printIconoUsuario.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/usuario.png"))
        self.ui_3.pushButton_2.setIcon(QIcon(f"{getcwd()}/setting_GUI/salida.png"))

    def eliminarCuenta(self):
        conexion = sqlite3.connect("login.db")
        cursor = conexion.cursor()
        opcion = QMessageBox().information(self, "Melnis", "¿Estas seguro que quieres eliminar esta cuenta?", QMessageBox.Yes, QMessageBox.No)
        if opcion == 16384:
            cursor.execute("DELETE FROM login WHERE Email=:email", {"email": self.ui_3.inputEmail.text()})
            self.close()
            self.ventanaInicio = Iniciar()
            self.ventanaInicio.show()
            del self
        conexion.commit()
        conexion.close()

    def cerrarSesion(self):
        self.close()
        self.ventana = Iniciar()
        self.ventana.show()
        del self

    def cambiarEmail(self):
        conexion = sqlite3.connect("login.db")
        email = QInputDialog().getText(Widgets(), "Milnes", "Introduzca su nuevo Email: ")
        if email[1]:
            cursor = conexion.cursor()
            cursor.execute("UPDATE login SET Email=? Where Email=? ", (email[0], self.ui_3.inputEmail.text()))
            self.ui_3.inputEmail.setText(email[0])
        conexion.commit()
        conexion.close()

    def cambiarUsuario(self):
        conexion = sqlite3.connect("login.db")
        usuario = QInputDialog().getText(Widgets(), "Milnes", "Introduzca su nuevo Usuario: ")
        if usuario[1]:
            cursor = conexion.cursor()
            cursor.execute("UPDATE login SET Usuario=? WHERE Usuario=? ", (usuario[0], self.ui_3.inputNombre.text()))
            self.ui_3.inputNombre.setText(usuario[0])
            self.ui_3.inputUsuarioMarco.setText(usuario[0])
        conexion.commit()
        conexion.close()

    def cambiarPassword(self):
        conexion = sqlite3.connect("login.db")
        password = QInputDialog().getText(Widgets(), "Milnes", "Introduzca su nueva Contraseña: ")
        if password[1]:
            cursor = conexion.cursor()
            cursor.execute("UPDATE login SET Password=? Where Password=? ", (password[0], self.ui_3.inputPassword.text()))
            self.ui_3.inputPassword.setText(password[0])
        conexion.commit()
        conexion.close()

    def cambiarApellidos(self):
        conexion = sqlite3.connect("login.db")
        apellidos = QInputDialog().getText(Widgets(), "Milnes", "Introduzca sus Nuevos Apellidos: ")
        if apellidos[1]:
            cursor = conexion.cursor()
            cursor.execute("UPDATE login SET Apellidos=? Where Apellidos=? ", (apellidos[0], self.ui_3.inputApellidos.text()))
            self.ui_3.inputApellidos.setText(apellidos[0])
        conexion.commit()
        conexion.close()

    def cambiarEdad(self):
        conexion = sqlite3.connect("login.db")
        edad = QInputDialog().getInt(Widgets(), "Milnes", "Introduzca su nueva Edad: ")
        if edad[1]:
            cursor = conexion.cursor()
            cursor.execute("UPDATE login SET Edad=? Where Edad=? ", (edad[0], self.ui_3.inputEdad.text()))
            self.ui_3.inputEdad.setText(str(edad[0]))
        conexion.commit()
        conexion.close()


class Crear(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Crear_Sesion()
        self.ui.setupUi(self)
        self.ui.imagen.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/fondoiniciar.jpg"))
        self.ui.boton_iniciar_sesion.clicked.connect(self.iniciar)
        self.ui.botosiguiente.clicked.connect(self.registrar)

    def registrar(self):
        nombre = self.ui.inputnombre.text()
        apellidos = self.ui.inputapellidos.text()
        email = self.ui.inputemail.text()
        password = self.ui.inputpassword.text()
        if nombre != "" and apellidos != "" and email != "" and password != "":
            try:
                edad = int(self.ui.inputedad.text())

            except ValueError:
                QMessageBox.critical(Widgets(), "Milnes", "Error No es Un Numero")
                self.ui.inputedad.setText("0")
            else:
                if edad != 0:
                    registrado = crear_sesion(nombre, apellidos, edad, email, password)

                    if registrado:
                        self.close()
                        self.ventana1 = Iniciar()
                        self.ventana1.show()
                        del self
        else:
            QMessageBox.critical(Widgets(), "Milnes", " Campos sin Rellenar")

    def iniciar(self):
        self.ventana1 = Iniciar()
        self.ventana1.show()
        self.close()
        del self


class Iniciar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Iniciar_Sesion()
        self.ui.setupUi(self)
        self.ui.imagen.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/fondoiniciar.jpg"))
        self.ui.botoncrearsesion.clicked.connect(self.crear)
        self.ui.botonsiguiente.clicked.connect(self.iniciarsesion)

    def iniciarsesion(self):
        email = self.ui.inputemail.text()
        password = self.ui.inputpassword.text()
        if email != "" and password != "":
            comprobar = login(email, password)
            if not comprobar[0]:
                QMessageBox.warning(self, "Milnes", "Email o Contraseña Incorrectas")
            else:
                self.ui3 = Inicio()
                self.ui3.ui_3.inputNombre.setText(f"{comprobar[1][2]}")
                self.ui3.ui_3.inputApellidos.setText(f"{comprobar[1][3]}")
                self.ui3.ui_3.inputEdad.setText(f"{comprobar[1][1]}")
                self.ui3.ui_3.inputEmail.setText(f"{comprobar[1][4]}")
                self.ui3.ui_3.inputPassword.setText(f"{comprobar[1][5]}")
                self.ui3.ui_3.inputUsuarioMarco.setText(f"{comprobar[1][2]}")
                self.close()
                self.ui3.show()
                del self

        else:
            QMessageBox.critical(Widgets(), "Milnes", " Campos sin Rellenar")

    def crear(self):
        self.ventana2 = Crear()
        self.ventana2.show()
        self.close()
        del self


class Widgets(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


def main():
    cmd = QApplication(argv)

    base_de_datos = Path("login.db")

    clase1 = Iniciar()

    if not base_de_datos.exists():
        QMessageBox.information(Widgets(), "Milnes", "\U0001f504" + " Configurando todo...")
        call("python setting_GUI/database/run_datebase.py")
        QMessageBox.information(Widgets(), "Milnes", "\u2714" + " Listo")

    clase1.show()
    exit(cmd.exec_())


if __name__ == '__main__':
    main()
