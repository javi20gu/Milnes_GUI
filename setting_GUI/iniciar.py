# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventiniciar.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Iniciar_Sesion(object):
    def setupUi(self, Iniciar_Sesion):
        Iniciar_Sesion.setObjectName("Iniciar_Sesion")
        Iniciar_Sesion.resize(611, 356)
        Iniciar_Sesion.setMinimumSize(QtCore.QSize(611, 356))
        Iniciar_Sesion.setMaximumSize(QtCore.QSize(611, 356))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Iniciar_Sesion.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        Iniciar_Sesion.setFont(font)
        self.marco = QtWidgets.QFrame(Iniciar_Sesion)
        self.marco.setGeometry(QtCore.QRect(0, 0, 611, 51))
        self.marco.setStyleSheet("background-color: rgb(36, 41, 46);")
        self.marco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.marco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.marco.setObjectName("marco")
        self.printMilnes = QtWidgets.QLabel(self.marco)
        self.printMilnes.setGeometry(QtCore.QRect(70, 0, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.printMilnes.setFont(font)
        self.printMilnes.setStyleSheet("color: rgb(255, 255, 255);")
        self.printMilnes.setObjectName("printMilnes")
        self.botoniniciarsesion = QtWidgets.QPushButton(self.marco)
        self.botoniniciarsesion.setGeometry(QtCore.QRect(360, 0, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.botoniniciarsesion.setFont(font)
        self.botoniniciarsesion.setStyleSheet("#botoniniciarsesion{\n"
"    color: rgb(142, 153, 154);\n"
"    border: 0px solid white;\n"
"}\n"
"")
        self.botoniniciarsesion.setObjectName("botoniniciarsesion")
        self.botonSalir = QtWidgets.QPushButton(self.marco)
        self.botonSalir.setGeometry(QtCore.QRect(0, 2, 71, 51))
        self.botonSalir.setStyleSheet("border: 0px solid black;")
        self.botonSalir.setText("")
        self.botonSalir.setIconSize(QtCore.QSize(46, 46))
        self.botonSalir.setObjectName("botonSalir")
        self.botoncrearsesion = QtWidgets.QPushButton(self.marco)
        self.botoncrearsesion.setGeometry(QtCore.QRect(480, 0, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.botoncrearsesion.setFont(font)
        self.botoncrearsesion.setStyleSheet("#botoncrearsesion::hover {\n"
"    border: 1px solid rgb(250, 250, 250);\n"
"    background-color:rgb(58, 63, 67);\n"
"    color: rgb(221, 238, 238);\n"
"}\n"
"#botoncrearsesion{\n"
"    color: rgb(214, 231, 232);\n"
"    border: 0px;\n"
"}\n"
"")
        self.botoncrearsesion.setObjectName("botoncrearsesion")
        self.printemail = QtWidgets.QLabel(Iniciar_Sesion)
        self.printemail.setGeometry(QtCore.QRect(190, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.printemail.setFont(font)
        self.printemail.setStyleSheet("color:  rgb(0, 12, 60);")
        self.printemail.setTextFormat(QtCore.Qt.PlainText)
        self.printemail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.printemail.setObjectName("printemail")
        self.inputemail = QtWidgets.QLineEdit(Iniciar_Sesion)
        self.inputemail.setGeometry(QtCore.QRect(190, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.inputemail.setFont(font)
        self.inputemail.setStyleSheet("border: 1px solid rgb(112, 112, 112);\n"
"color: rgb(25, 25, 25);\n"
"background-color:rgba(226, 170, 123, .4);\n"
"border-radius: 3px 3px 3px 3px;")
        self.inputemail.setMaxLength(500)
        self.inputemail.setAlignment(QtCore.Qt.AlignCenter)
        self.inputemail.setClearButtonEnabled(True)
        self.inputemail.setObjectName("inputemail")
        self.inputpassword = QtWidgets.QLineEdit(Iniciar_Sesion)
        self.inputpassword.setGeometry(QtCore.QRect(190, 180, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setItalic(False)
        self.inputpassword.setFont(font)
        self.inputpassword.setStyleSheet("border: 1px solid rgb(112, 112, 112);\n"
"background-color:  rgba(226, 170, 123, .4);\n"
"color: rgb(25, 25, 25);\n"
"border-radius: 3px 3px 3px 3px;r")
        self.inputpassword.setText("")
        self.inputpassword.setMaxLength(800)
        self.inputpassword.setFrame(True)
        self.inputpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputpassword.setAlignment(QtCore.Qt.AlignCenter)
        self.inputpassword.setClearButtonEnabled(True)
        self.inputpassword.setObjectName("inputpassword")
        self.printpassword = QtWidgets.QLabel(Iniciar_Sesion)
        self.printpassword.setGeometry(QtCore.QRect(190, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.printpassword.setFont(font)
        self.printpassword.setStyleSheet("color:  rgb(0, 12, 60);;")
        self.printpassword.setTextFormat(QtCore.Qt.PlainText)
        self.printpassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.printpassword.setObjectName("printpassword")
        self.botonsiguiente = QtWidgets.QPushButton(Iniciar_Sesion)
        self.botonsiguiente.setGeometry(QtCore.QRect(240, 260, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.botonsiguiente.setFont(font)
        self.botonsiguiente.setStyleSheet("#botonsiguiente{\n"
"background-color: rgba(36, 41, 46, .9);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"#botonsiguiente::hover{\n"
"    background-color: rgba(243, 221, 202, .8);\n"
"    color: rgb(58, 63, 67);\n"
"    border: 2px solid rgb(255, 232, 212);\n"
"}")
        self.botonsiguiente.setObjectName("botonsiguiente")
        self.imagen = QtWidgets.QLabel(Iniciar_Sesion)
        self.imagen.setGeometry(QtCore.QRect(0, 50, 611, 311))
        self.imagen.setText("")
        self.imagen.setObjectName("imagen")
        self.imagen.raise_()
        self.marco.raise_()
        self.printemail.raise_()
        self.inputemail.raise_()
        self.inputpassword.raise_()
        self.printpassword.raise_()
        self.botonsiguiente.raise_()

        self.retranslateUi(Iniciar_Sesion)
        QtCore.QMetaObject.connectSlotsByName(Iniciar_Sesion)

    def retranslateUi(self, Iniciar_Sesion):
        _translate = QtCore.QCoreApplication.translate
        Iniciar_Sesion.setWindowTitle(_translate("Iniciar_Sesion", "Minles"))
        self.printMilnes.setText(_translate("Iniciar_Sesion", "Milnes"))
        self.botoniniciarsesion.setText(_translate("Iniciar_Sesion", "Iniciar Sesión"))
        self.botoncrearsesion.setText(_translate("Iniciar_Sesion", "Crear Sesión"))
        self.printemail.setText(_translate("Iniciar_Sesion", "Email:"))
        self.inputemail.setPlaceholderText(_translate("Iniciar_Sesion", "Introduce Email"))
        self.inputpassword.setPlaceholderText(_translate("Iniciar_Sesion", "Introduce Contraseña"))
        self.printpassword.setText(_translate("Iniciar_Sesion", "Password:"))
        self.botonsiguiente.setText(_translate("Iniciar_Sesion", "Siguiente"))

