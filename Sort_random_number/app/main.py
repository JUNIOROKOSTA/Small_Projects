from functools import cache
from scipy.__config__ import show
from app_sort_random_number import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5 import QtWidgets
import sys
import random

class  AAplication(QWidget, Ui_MainWindow):
    def __init__(self) -> None:
        super(AAplication,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('App')

        self.action_btn.clicked.connect(self.show_display)
        self.msn_error = "Preencha os campos \nsomente com Números."
    
    def show_display(self):
        try:
            self.min = int(self.min_num.text())
            self.max = int(self.max_num.text())
            self.qtd = int(self.qtd_num.text())
            
            numbersList = self.random_sort(self.min, self.max, self.qtd)
            numbersList = str(numbersList).strip('[]')
            self.display_output.setText(numbersList)
        except :
            self.display_output.setText(self.msn_error)
        
    def random_sort(self,min, max, qtd):
        try:
            lista_random = random.sample(range(min, max+1),qtd)
            lista_random = sorted(lista_random)
            return lista_random
        except :
            self.display_output.setText(self.msn_error)


    




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AAplication()
    window.show()
    sys.exit(app.exec_())


