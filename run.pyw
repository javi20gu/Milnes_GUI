from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap, QIcon
from sys import exit, argv
from pathlib import Path
from os import getcwd
from setting_GUI.database.run_datebase import Database
from setting_GUI import *


class Inicio(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_3 = Ui_Inicio()
        self.ui_3.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui_3.botonEmail.clicked.connect(self.cambiarEmail)
        self.ui_3.botonPassword.clicked.connect(self.cambiarPassword)
        self.ui_3.botonNombre.clicked.connect(self.cambiarUsuario)
        self.ui_3.botonApellidos.clicked.connect(self.cambiarApellidos)
        self.ui_3.botonEdad.clicked.connect(self.cambiarEdad)
        self.ui_3.botonCerrarSesion.clicked.connect(self.cerrarSesion)
        self.ui_3.botonSalir.clicked.connect(self.eliminarCuenta)
        self.ui_3.flecha1.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/flecha.png"))
        self.ui_3.flecha2.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/flecha.png"))
        self.ui_3.flecha3.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/flecha.png"))
        self.ui_3.flecha4.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/flecha.png"))
        self.ui_3.flecha5.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/flecha.png"))
        self.ui_3.botonSalir.setIcon(QIcon(f"{getcwd()}/setting_GUI/borrar.png"))
        self.ui_3.printIconoUsuario.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/usuario.png"))
        self.ui_3.botonCerrarSesion.setIcon(QIcon(f"{getcwd()}/setting_GUI/salida.png"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def eliminarCuenta(self):
        opcion = QtWidgets.QMessageBox().information(self, "Melnis", "¿Estas seguro que quieres eliminar esta cuenta?",
                                                     QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if opcion == 16384:
            Database().eliminar_cuenta(self.ui_3.inputEmail.text())
            self.close()
            self.ventanaInicio = Iniciar()
            self.ventanaInicio.show()
            del self

    def cerrarSesion(self):
        self.close()
        self.ventana = Iniciar()
        self.ventana.show()
        del self

    def cambiarEmail(self):
        email = QtWidgets.QInputDialog().getText(self, "Milnes", "Introduzca su nuevo Email: ")

        if email[1]:
            noproblema = Database().cambiar_email(self.ui_3.inputEmail.text(), email[0])
            if noproblema:
                self.ui_3.inputEmail.setText(email[0])

    def cambiarUsuario(self):
        usuario = QtWidgets.QInputDialog().getText(self, "Milnes", "Introduzca su nuevo Usuario: ")

        if usuario[1]:
            Database().cambiar_usuario(self.ui_3.inputNombre.text(), usuario[0])
            self.ui_3.inputNombre.setText(usuario[0])
            self.ui_3.inputUsuarioMarco.setText(usuario[0])

    def cambiarPassword(self):
        password = QtWidgets.QInputDialog().getText(self, "Milnes", "Introduzca su nueva Contraseña: ")

        if password[1]:
            Database().cambiar_password(self.ui_3.inputPassword.text(), password[0])
            self.ui_3.inputPassword.setText(password[0])

    def cambiarApellidos(self):
        apellidos = QtWidgets.QInputDialog().getText(self, "Milnes", "Introduzca sus Nuevos Apellidos: ")

        if apellidos[1]:
            Database().cambiar_apellidos(self.ui_3.inputApellidos.text(), apellidos[0])
            self.ui_3.inputApellidos.setText(apellidos[0])

    def cambiarEdad(self):
        edad = QtWidgets.QInputDialog().getInt(self, "Milnes", "Introduzca su nueva Edad: ")

        if edad[1]:
            Database.cambiar_edad(self.ui_3.inputEdad.text(), edad[0])
            self.ui_3.inputEdad.setText(str(edad[0]))


class Crear(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Crear_Sesion()
        self.ui.setupUi(self)
        self.setWindowFlags((Qt.FramelessWindowHint))
        self.ui.imagen.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/crear.jpg"))
        self.ui.botonSalir.setIcon(QIcon(f"{getcwd()}/setting_GUI/salir.ico"))
        self.ui.boton_iniciar_sesion.clicked.connect(self.iniciar)
        self.ui.botosiguiente.clicked.connect(self.registrar)
        self.ui.botonSalir.clicked.connect(self.salirApp)

    def salirApp(self):
        self.close()
        del self
        exit()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def registrar(self):
        nombre = self.ui.inputnombre.text()
        apellidos = self.ui.inputapellidos.text()
        email = self.ui.inputemail.text()
        password = self.ui.inputpassword.text()
        if nombre != "" and apellidos != "" and email != "" and password != "":
            try:
                edad = int(self.ui.inputedad.text())

            except ValueError:
                QtWidgets.QMessageBox.critical(self, "Milnes", "Error No es Un Numero")
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
            QtWidgets.QMessageBox.critical(self, "Milnes", " Campos sin Rellenar")

    def iniciar(self):
        self.ventana1 = Iniciar()
        self.ventana1.show()
        self.close()
        del self


class Iniciar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Iniciar_Sesion()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.imagen.setPixmap(QPixmap(f"{getcwd()}/setting_GUI/fondoiniciar.jpg"))
        self.ui.botonSalir.setIcon(QIcon(f"{getcwd()}/setting_GUI/salir.ico"))
        self.ui.botoncrearsesion.clicked.connect(self.crear)
        self.ui.botonsiguiente.clicked.connect(self.iniciarsesion)
        self.ui.botonSalir.clicked.connect(self.salirApp)

    def salirApp(self):
        self.close()
        del self
        exit()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def iniciarsesion(self):
        email = self.ui.inputemail.text()
        password = self.ui.inputpassword.text()
        if email != "" and password != "":
            comprobar = login(email, password)
            if not comprobar[0]:
                QtWidgets.QMessageBox.warning(self, "Milnes", "Email o Contraseña Incorrectas")
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
            QtWidgets.QMessageBox.critical(self, "Milnes", " Campos sin Rellenar")

    def crear(self):
        self.ventana2 = Crear()
        self.ventana2.show()
        self.close()
        del self


def main():
    cmd = QtWidgets.QApplication(argv)

    base_de_datos = Path("login.db")

    clase1 = Iniciar()

    if not base_de_datos.exists():
        QtWidgets.QMessageBox.information(QtWidgets.QWidget(), "Milnes", "\U0001f504" + " Configurando todo...")
        from setting_GUI.database import Database
        Database.create()
        QtWidgets.QMessageBox.information(QtWidgets.QWidget(), "Milnes", "\u2714" + " Listo")

    clase1.show()
    exit(cmd.exec_())


if __name__ == '__main__':
    main()
