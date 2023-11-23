from PyQt5 import QtWidgets, uic
import sympy as sp
import sys

app = QtWidgets.QApplication([])
inicio = uic.loadUi("Proyecto1.ui")
entrar = uic.loadUi("U3.ui")
error = uic.loadUi("U2.ui")
registro = uic.loadUi("U1.ui")
x = sp.symbols('x')

def gui_login():
    usser = inicio.lineEdit.text()
    password = inicio.lineEdit_2.text()
    if len(usser)==0 or len(password)==0:
        inicio.label_2.setText("ENTER DATE")
    elif usser == "nf833949@gmail.com" and password == "2123":
        gui_entrar()
    else:
        gui_error()

def gui_contacto():
    nombre = registro.lineEdit.text()
    apellido= registro.lineEdit_2.text()
    email= registro.lineEdit_3.text()
    contrasena= registro.lineEdit_4.text()
    if len(nombre)==0 or len(apellido)==0 or len(email)== 0 or len(contrasena)==0:
        registro.dato.setText("Enter Date")
    else:
        registro.dato.setText("  ")
        registro.dato_2.setText("data recorded")



def factoreo():
        expresion = entrar.ejercicio.text()
        ejercicio.factores.connect()
        factores = sp.factor(expresion)
        print(factores)

def gui_entrar():
        inicio.hide()
        entrar.show()
def gui_error():
    inicio.hide()
    error.show()
def regresar_entrar():
    entrar.hide()
    inicio.show()


def gui_registro():
    inicio.hide()
    registro.show()


def regresar_login():
        registro.hide()
        inicio.show()
def regresar_error():
        error.hide()
        inicio.show()


inicio.pushButton.clicked.connect(gui_login)
entrar.pushButton.clicked.connect(regresar_entrar)
error.pushButton.clicked.connect(regresar_error)
inicio.commandLinkButton.clicked.connect(gui_registro)
registro.pushButton_2.clicked.connect(regresar_login)
entrar.calculo.clicked.connect(factoreo)
registro.pushButton.clicked.connect(gui_contacto)

inicio.show()
app.exec()