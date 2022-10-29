import sys
from view_style.windows import Ui_MainWindow
from banco.connect_db import VProduces
from utils.date_utils import data_format, data_now
from PyQt5.QtWidgets import QMainWindow,QApplication, QTableWidgetItem
from PyQt5.QtGui import QIcon, QPixmap


class SisVendas(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.path_img = 'view_style/img/'
        self.setWindowTitle('Sistema de Vendas')
        self.setWindowIcon(QIcon('view_style/img/iconi.png'))
        self.fruits_values = []
        self.banc = 'banco/vprodutos.db'

        self.frutas, self.valores = self.charge_fruits()
        self.clients_values =[]
        self.clients_all = []
        self.edite = ''
        self.charge_clients()


        self.coBox_product.addItems(self.frutas)

        self.coBox_client.addItems(self.clients_values)

        self.vendas = []
        self.valores = dict(self.fruits_values)

        self.pB_add_car.clicked.connect(self.add_car)

        self.coBox_product.activated.connect(self.img_fruit)

        self.pushB_limpar.clicked.connect(self.clear_car)

        self.pushB_apagar.clicked.connect(self.delet_product)

        self.pushB_comprar.clicked.connect(self.product_buy)

        self.pushB_consultar.clicked.connect(self.consult_venda)

        self.pushB_cadastrar_cliente.clicked.connect(self.cadastra_cliente)

        self.pushB_delet_cliente.clicked.connect(self.delet_client)

        self.pushB_edit_cliente.clicked.connect(self.update_client)

        self.table_cliente.clicked.connect(self.get_client)

        self.label_hoje.setText(data_format())

        self.img_fruit()



    def add_car(self):

        cliente = self.coBox_client.currentText()
        produt = self.coBox_product.currentText()
        peso = self.lineEdit_peso.text()
        peso = str(float(peso.replace(',','.')))
        valor = self.calc_valor(produt, peso)
        datar = data_now()

        self.vendas.append({'Cliente': cliente, 'Produto': produt,
                            'Peso': peso, 'Valor': valor, 'Data': datar})
        self.show_product()

    def show_product(self):

        tm = len(self.vendas)
        self.table_center.setRowCount(tm)
        rows = 0

        for venda in self.vendas:
            self.table_center.setItem(rows, 0, QTableWidgetItem(venda['Cliente']))
            self.table_center.setItem(rows, 1, QTableWidgetItem(venda['Produto']))
            self.table_center.setItem(rows, 2, QTableWidgetItem(venda['Peso']))
            self.table_center.setItem(rows, 3, QTableWidgetItem(venda['Valor']))
            self.table_center.setItem(rows, 4, QTableWidgetItem(venda['Data']))

            rows+=1

    def img_fruit(self):
        fruit = self.coBox_product.currentText().lower()
        fruit = self.path_img + fruit + '.png'
        self.label_img.setPixmap(QPixmap(fruit))
        self.label_img.setScaledContents(True)
        self.label_preco.setText(str(self.valores[self.coBox_product.currentText()]))

    def calc_valor(self, product, peso):
        valor = self.valores[product] * float(peso.replace(',','.'))
        return str(round(valor,2))

    def clear_car(self):
        self.vendas = []
        self.show_product()

    def delet_product(self):
        try:
            position = self.table_center.currentRow()
            self.vendas.pop(position)
            self.show_product()
        except Exception as error:
            pass

    def product_buy(self):
        for venda in self.vendas:
            cliente = venda['Cliente']
            produto = venda['Produto']
            peso = venda['Peso']
            valor = venda['Valor']
            datar = venda['Data']

            buy = VProduces(self.banc)
            buy.insert_into(cliente, produto, peso, valor, datar)

        self.clear_car()


    def charge_fruits(self):
        fruits = VProduces(self.banc)
        self.fruits_values = fruits.get_fruits()

        frutas = [x[0] for x in self.fruits_values]
        valores = [x[1] for x in self.fruits_values]

        return frutas, valores

    def charge_clients(self):
        clientes = VProduces(self.banc)
        self.clients_all = clientes.get_clients()
        self.clients_values = [x[1] for x in self.clients_all]
        self.show_clientes(self.clients_all)

    def consult_venda(self):
        vendas = VProduces(self.banc)
        nome = self.lineE_consult_nome.text()
        data_c = self.dateE_consulta.text()
        delta = []

        if data_c =='01/01/2000' and nome == '':
            delta = vendas.get_vendas()

        elif data_c =='01/01/2000':
            delta = vendas.get_vendas_where_name(nome)

        elif data_c != '01/01/2000':
            delta = vendas.get_vendas_where_name_date(nome, data_c)

        self.show_vendas(delta)


    def show_vendas(self,result_consult):
        t_vendas = result_consult
        tm = len(t_vendas)
        self.table_cunsulta.setRowCount(tm)
        rows = 0

        for venda in t_vendas:
            self.table_cunsulta.setItem(rows, 0, QTableWidgetItem(str(venda[0])))
            self.table_cunsulta.setItem(rows, 1, QTableWidgetItem(venda[1]))
            self.table_cunsulta.setItem(rows, 2, QTableWidgetItem(venda[2]))
            self.table_cunsulta.setItem(rows, 3, QTableWidgetItem(venda[3]))
            self.table_cunsulta.setItem(rows, 4, QTableWidgetItem(str(venda[4])))
            self.table_cunsulta.setItem(rows, 5, QTableWidgetItem(venda[5]))

            rows+=1

    def show_clientes(self,result_consult):
        t_vendas = result_consult
        tm = len(t_vendas)
        self.table_cliente.setRowCount(tm)
        rows = 0

        for venda in t_vendas:

            self.table_cliente.setItem(rows, 0, QTableWidgetItem(str(venda[0])))
            self.table_cliente.setItem(rows, 1, QTableWidgetItem(venda[1]))
            self.table_cliente.setItem(rows, 2, QTableWidgetItem(str(venda[2])))

            rows+=1

    def cadastra_cliente(self):
        try:
            nome = self.lineE_nome_cliente.text()
            idade = int(self.lineE_idade_cliente.text())
            if nome != '' and idade != '':
                cliente = VProduces(self.banc)
                cliente.insert_client_into(nome,idade)
        except Exception as error:
            pass

        self.charge_clients()
        self.clear_c_client()


    def get_client(self):
        try:
            position = self.table_cliente.currentRow()
            self.edite = self.clients_all[position]
            self.lineE_nome_cliente.setText(self.edite[1])
            self.lineE_idade_cliente.setText(str(self.edite[2]))
        except Exception as error:
            pass

    def clear_c_client(self):
        self.lineE_idade_cliente.setText('')
        self.lineE_nome_cliente.setText('')

    def update_client(self):
        try:
            cliente_edit = VProduces(self.banc)

            idr=self.edite[0]
            nome= self.lineE_nome_cliente.text()
            idade= self.lineE_idade_cliente.text()

            cliente_edit.update_cliente(nome,idade,idr)

            self.clear_c_client()
            self.charge_clients()
        except Exception as error:
            pass

    def delet_client(self):
        try:
            cliente_edit = VProduces(self.banc)
            cliente_edit.delete_client(self.edite[0])

            self.clear_c_client()
            self.charge_clients()
        except Exception as error:
            pass




if __name__ == '__main__':

    qt = QApplication(sys.argv)
    app = SisVendas()
    app.show()
    qt.exec_()
