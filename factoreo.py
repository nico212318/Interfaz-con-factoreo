from PyQt5 import QtWidgets, uic
import sys
import sympy as sp

x = sp.symbols('x')

class Ui(QtWidgets.QMainWindow):
    def _init_(self):
        super(Ui, self)._init_()
        uic.loadUi('U3.ui', self)
        self.calculo.clicked.connect(self.factoreo)
        self.show()

    def factoreo(self):
        expresion = self.ejercicio.text()
        factores = sp.factor(expresion)
        self.imprimir_resultado(factores)

    def imprimir_resultado(self, resultado):
        self.resultado.setText(str(resultado))

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()