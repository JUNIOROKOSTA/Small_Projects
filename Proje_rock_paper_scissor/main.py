from ui_game import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
import sys
import random


class  App_Game(QWidget, Ui_MainWindow):
    def __init__(self) -> None:
        super(App_Game,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('App')

    # Action button

        self.pedra_btn.clicked.connect(self.pedra)
        self.tesoura_btn.clicked.connect(self.tesoura)
        self.papel_btn.clicked.connect(self.papel)

    def pedra(self):
        self.main("pedra")

    def tesoura(self):
        self.main("tesoura")
    
    def papel(self):
        self.main("papel")

    def main(self,hand):

        player = hand
        computer = random.choice(['papel','pedra','tesoura'])
        self.msn_c = str("Ecolha do computador :\n"+computer)


        if computer == player:
            self.show_display('Empate!')
            return 
    
        win = self.winners(player,computer)

        if win:

            self.show_display("Vaocê ganhou!")
            return 

        self.show_display('Você perdeu.')
        return

    def winners(self,player,computer):
        if (player == 'papel' and computer == 'pedra') \
            or (player == 'tesoura' and computer == 'papel') \
            or (player == 'pedra' and computer == 'tesoura'):
            return True
    
        return False
    
    def show_display(self,msn):
        self.output_display_2.setText(self.msn_c)
        self.output_display.setText(msn)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App_Game()
    window.show()
    sys.exit(app.exec_())


