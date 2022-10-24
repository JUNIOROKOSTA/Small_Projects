import sys
import os
from time import sleep
from pathlib import Path
from window_app import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle('Size_Image')

        self.diretorio = ''
        self.destino = ''
        self.pb_buscar_pasta.clicked.connect(self.caminho_origem)
        self.pb_pasta_destino.clicked.connect(self.caminho_destino)
        self.pb_salvar.clicked.connect(self.salvar_alt)

    def load_img(self):
        diretorio = QFileDialog.getExistingDirectory(
            self.centralwidget,
            'Escolher Imagem',)
        return diretorio

    def caminho_origem(self):
        origem = self.load_img()
        self.diretorio = Path(origem)
        origem = str(self.diretorio)
        self.le_caminho.setText(origem)

    def caminho_destino(self):
        origem = self.load_img()
        self.destino = Path(origem)
        origem = str(self.destino)
        self.le_destino.setText(origem)

    def salvar_alt(self):
        try:
            novo_tamanho = int(self.le_tamanho.text())
        except Exception as e:
            print("Erro novo tamanho")
        self.destino = self.le_destino.text()

        for roots, dicts, files in os.walk(self.diretorio):
            self.ProBar.setMinimum(0)
            self.ProBar.setMaximum(len(files))
            v = 0
            for file in files:
                caminho = os.path.join(roots, file)
                img = QPixmap(caminho)
                try:
                    new_img = img.scaledToWidth(novo_tamanho)
                    tamanho = f'{new_img.width()} x {new_img.height()}'
                    name, ext = file.split('.')
                    name = f'{name}_{tamanho}_.{ext}'
                    dest = os.path.join(self.destino, name)
                    new_img.save(dest, 'PNG')

                except Exception as error:
                    print("def resize_img ERROR: ", error)
                sleep(0.05)
                v += 1
                self.ProBar.setValue(v)
                sleep(0.01)
                self.lb_titulo.setText(name)

        self.le_destino.setText('Completo')
        self.le_caminho.setText('Completo')


if __name__ == '__main__':
    aplication = QApplication(sys.argv)
    app = App()
    app.show()
    try:
        sys.exit(aplication.exec_())
    except SystemError:
        print('Closing window...')
