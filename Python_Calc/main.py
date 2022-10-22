from PySide2.QtWidgets import (QApplication, QMainWindow)
from py_calc import Ui_Calculadora_Qt
import sys


class Window(QMainWindow, Ui_Calculadora_Qt):
    def __init__(self) -> None:
        super(Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Okosta Calculadora")

        self.total = ""

        self.btn_1.clicked.connect(lambda: self.calc(1))
        self.btn_2.clicked.connect(lambda: self.calc(2))
        self.btn_3.clicked.connect(lambda: self.calc(3))
        self.btn_4.clicked.connect(lambda: self.calc(4))
        self.btn_5.clicked.connect(lambda: self.calc(5))
        self.btn_6.clicked.connect(lambda: self.calc(6))
        self.btn_7.clicked.connect(lambda: self.calc(7))
        self.btn_8.clicked.connect(lambda: self.calc(8))
        self.btn_9.clicked.connect(lambda: self.calc(9))
        self.btn_0.clicked.connect(lambda: self.calc(0))
        self.btn_ponto.clicked.connect(lambda: self.calc("."))
        self.btn_soma.clicked.connect(lambda: self.calc("+"))
        self.btn_subri.clicked.connect(lambda: self.calc("-"))
        self.btn_multiplica.clicked.connect(lambda: self.calc("*"))
        self.btn_dividir.clicked.connect(lambda: self.calc("/"))
        self.btn_igual.clicked.connect(lambda: self.resultShow(self.total))
        self.btn_ce.clicked.connect(lambda: self.cClear())
        self.btn_c.clicked.connect(lambda: self.clearAll())

    def clearAll(self):
        self.total = ""
        self.visorShow(self.total)

    def cClear(self):
        self.total = self.total[:-1]
        self.visorShow(self.total)

    def calc(self, valor):
        self.total += (str(valor))
        self.visorShow(self.total)

    def resultShow(self, x):
        try:
            resulte = eval(x)
            self.total = str(resulte)
            self.visorShow(resulte)
        except Exception as err:
            self.clearAll()
            self.visorShow('ERROR!!!')

    def visorShow(self, number):
        self.painel.setText(str(number))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
