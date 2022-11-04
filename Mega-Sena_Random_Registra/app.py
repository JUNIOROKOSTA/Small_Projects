import sys
import random
from turtle import position
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from tela import Ui_MainWindow
from PyQt5.QtGui import QIcon, QPixmap

from webresult import WebReq
from action_db import Request_DB


class AAplication(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(AAplication, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('App-Apostas')
        self.web_request = WebReq()
        self.img_path = r'img\mega-sena-logo.png'

        self.obter_ultmo_result()
        self.show_table()
        self.carregar_img()

        self.pb_gerar_sorte.clicked.connect(self.random_sort)
        self.pb_registrar_sorte.clicked.connect(self.registra)
        self.pb_resultado.clicked.connect(self.atualizar_table)

    def conecta(self):
        request_db = Request_DB('registros_db.db')
        return request_db

    def format_aposta(self, nume):
        numberR = str(nume).replace(', ', '-')
        numberR = numberR.replace("'", '')
        numberR = numberR.replace('[', '')
        numberR = numberR.replace(']', '')
        return numberR

    def carregar_img(self):
        self.label_imagem.setPixmap(QPixmap(self.img_path))
        self.label_imagem.setScaledContents(True)

    def random_sort(self):
        try:
            lista_random = random.sample(range(1, 60+1), 6)
            lista_random = sorted(lista_random)
            aposta = self.format_aposta(lista_random)
            self.le_aposta_sorte.setText(aposta)
            self.lb_msn.setText('Aposta Gerada, Boa Sorte!')
            return lista_random
        except:
            self.lb_msn.setText('Error... Tente novamente!')

    def obter_ultmo_result(self):
        prox_c, data_prox_c, valor_ = self.web_request.ultimo_concurso()

        self.le_Concurso.setText(str(prox_c))
        self.le_Data.setText(str(data_prox_c))

    def registra(self):

        data = self.le_Data.text()
        concurso = self.le_Concurso.text()
        aposta = self.le_aposta_sorte.text()

        db = self.conecta()
        if db.verific_aposta(concurso, aposta):
            self.lb_msn.setText('Já existe essa aposta registrada.')
            return

        db = self.conecta()
        db.insert_into(concurso, aposta, data)
        self.show_table()

        self.lb_msn.setText(f'Aposta "{aposta}" Registrada com Sucesso!')

    def show_table(self):
        db = self.conecta()
        colunas = db.get_apostas()
        self.res_tabela = colunas
        tm = len(colunas)
        self.tabela.setRowCount(tm)
        linha = 0

        for coluna in colunas:

            self.tabela.setItem(linha, 0, QTableWidgetItem(coluna[0]))
            self.tabela.setItem(linha, 1, QTableWidgetItem(coluna[1]))
            self.tabela.setItem(linha, 2, QTableWidgetItem(coluna[2]))
            self.tabela.setItem(linha, 3, QTableWidgetItem(coluna[3]))
            self.tabela.setItem(linha, 4, QTableWidgetItem(coluna[4]))
            self.tabela.setItem(linha, 5, QTableWidgetItem(coluna[5]))

            linha += 1

    def position(self):
        posit = self.tabela.currentRow()
        return posit

    def check_acertos(self, ap1, ap2):
        ap1_ = ap1.split('-')
        ap2_ = ap2.split('-')
        resulta = [x in ap1_ for x in ap2_]
        resulta = resulta.count(True)
        return str(resulta)

    def atualizar_table(self):
        try:
            posit = self.position()
            concurso = self.res_tabela[posit][0]
            aposta = self.res_tabela[posit][1]

            dezenas, premio = self.web_request.consultar_concurso(concurso)
            dezenas = self.format_aposta(dezenas)

            acertos = self.check_acertos(dezenas, aposta)

            if premio == '-':
                premio = 'Acumulou'

            db = self.conecta()
            db.update_table(dezenas, premio, acertos,
                            concurso=concurso, aposta=aposta)
        except:
            self.lb_msn.setText('Não foi encontrado dados para esse registro.')

        self.show_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AAplication()
    window.show()
    sys.exit(app.exec_())


"""
06-07-11-20-30-34
03-06-15-23-24-33
04-07-08-26-28-35
01-03-24-37-51-55
"""
