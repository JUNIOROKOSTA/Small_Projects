# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 896)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_center = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_center.setObjectName("tab_center")
        self.tab_vendas = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Noto Sans Lao")
        font.setPointSize(12)
        self.tab_vendas.setFont(font)
        self.tab_vendas.setObjectName("tab_vendas")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_vendas)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.table_center = QtWidgets.QTableWidget(self.tab_vendas)
        self.table_center.setMinimumSize(QtCore.QSize(520, 0))
        self.table_center.setObjectName("table_center")
        self.table_center.setColumnCount(5)
        self.table_center.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_center.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_center.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_center.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_center.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_center.setHorizontalHeaderItem(4, item)
        self.gridLayout_2.addWidget(self.table_center, 4, 0, 1, 7)
        self.label_img = QtWidgets.QLabel(self.tab_vendas)
        self.label_img.setMaximumSize(QtCore.QSize(160, 160))
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setObjectName("label_img")
        self.gridLayout_2.addWidget(self.label_img, 0, 5, 4, 2)
        self.label_4 = QtWidgets.QLabel(self.tab_vendas)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 3, 1, 1)
        self.label_client = QtWidgets.QLabel(self.tab_vendas)
        self.label_client.setObjectName("label_client")
        self.gridLayout_2.addWidget(self.label_client, 0, 0, 1, 1)
        self.coBox_product = QtWidgets.QComboBox(self.tab_vendas)
        self.coBox_product.setObjectName("coBox_product")
        self.gridLayout_2.addWidget(self.coBox_product, 1, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.tab_vendas)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 1, 1, 1)
        self.label_preco = QtWidgets.QLabel(self.tab_vendas)
        self.label_preco.setText("")
        self.label_preco.setObjectName("label_preco")
        self.gridLayout_2.addWidget(self.label_preco, 1, 4, 1, 1)
        self.label_weight_2 = QtWidgets.QLabel(self.tab_vendas)
        self.label_weight_2.setObjectName("label_weight_2")
        self.gridLayout_2.addWidget(self.label_weight_2, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_vendas)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 6, 1, 1)
        self.lineEdit_peso = QtWidgets.QLineEdit(self.tab_vendas)
        self.lineEdit_peso.setObjectName("lineEdit_peso")
        self.gridLayout_2.addWidget(self.lineEdit_peso, 2, 1, 1, 3)
        self.label_produt_preco = QtWidgets.QLabel(self.tab_vendas)
        self.label_produt_preco.setObjectName("label_produt_preco")
        self.gridLayout_2.addWidget(self.label_produt_preco, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_vendas)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 6, 5, 1, 1)
        self.label_produt = QtWidgets.QLabel(self.tab_vendas)
        self.label_produt.setObjectName("label_produt")
        self.gridLayout_2.addWidget(self.label_produt, 1, 0, 1, 1)
        self.coBox_client = QtWidgets.QComboBox(self.tab_vendas)
        self.coBox_client.setObjectName("coBox_client")
        self.gridLayout_2.addWidget(self.coBox_client, 0, 1, 1, 2)
        self.pB_add_car = QtWidgets.QPushButton(self.tab_vendas)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pB_add_car.setFont(font)
        self.pB_add_car.setObjectName("pB_add_car")
        self.gridLayout_2.addWidget(self.pB_add_car, 3, 1, 1, 3)
        self.label_kg = QtWidgets.QLabel(self.tab_vendas)
        self.label_kg.setObjectName("label_kg")
        self.gridLayout_2.addWidget(self.label_kg, 2, 4, 1, 1)
        self.pushB_comprar = QtWidgets.QPushButton(self.tab_vendas)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushB_comprar.setFont(font)
        self.pushB_comprar.setObjectName("pushB_comprar")
        self.gridLayout_2.addWidget(self.pushB_comprar, 6, 0, 1, 1)
        self.pushB_limpar = QtWidgets.QPushButton(self.tab_vendas)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushB_limpar.setFont(font)
        self.pushB_limpar.setObjectName("pushB_limpar")
        self.gridLayout_2.addWidget(self.pushB_limpar, 6, 2, 1, 1)
        self.pushB_apagar = QtWidgets.QPushButton(self.tab_vendas)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushB_apagar.setFont(font)
        self.pushB_apagar.setObjectName("pushB_apagar")
        self.gridLayout_2.addWidget(self.pushB_apagar, 6, 4, 1, 1)
        self.tab_center.addTab(self.tab_vendas, "")
        self.tab_consult_vendas = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Noto Sans Lao")
        font.setPointSize(12)
        self.tab_consult_vendas.setFont(font)
        self.tab_consult_vendas.setObjectName("tab_consult_vendas")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_consult_vendas)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_consult_nome = QtWidgets.QLabel(self.tab_consult_vendas)
        self.label_consult_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_consult_nome.setObjectName("label_consult_nome")
        self.gridLayout_3.addWidget(self.label_consult_nome, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_consult_vendas)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.label_consult_data = QtWidgets.QLabel(self.tab_consult_vendas)
        self.label_consult_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_consult_data.setObjectName("label_consult_data")
        self.gridLayout_3.addWidget(self.label_consult_data, 3, 0, 1, 1)
        self.dateE_consulta = QtWidgets.QDateEdit(self.tab_consult_vendas)
        self.dateE_consulta.setObjectName("dateE_consulta")
        self.gridLayout_3.addWidget(self.dateE_consulta, 3, 1, 1, 1)
        self.lineE_consult_nome = QtWidgets.QLineEdit(self.tab_consult_vendas)
        self.lineE_consult_nome.setObjectName("lineE_consult_nome")
        self.gridLayout_3.addWidget(self.lineE_consult_nome, 2, 1, 1, 1)
        self.pushB_consultar = QtWidgets.QPushButton(self.tab_consult_vendas)
        self.pushB_consultar.setObjectName("pushB_consultar")
        self.gridLayout_3.addWidget(self.pushB_consultar, 2, 3, 2, 1)
        self.table_cunsulta = QtWidgets.QTableWidget(self.tab_consult_vendas)
        self.table_cunsulta.setMinimumSize(QtCore.QSize(600, 0))
        self.table_cunsulta.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_cunsulta.setObjectName("table_cunsulta")
        self.table_cunsulta.setColumnCount(6)
        self.table_cunsulta.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_cunsulta.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cunsulta.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cunsulta.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cunsulta.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cunsulta.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cunsulta.setHorizontalHeaderItem(5, item)
        self.gridLayout_3.addWidget(self.table_cunsulta, 4, 0, 1, 4)
        self.tab_center.addTab(self.tab_consult_vendas, "")
        self.tab_cadast_client = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Noto Sans Lao")
        font.setPointSize(12)
        self.tab_cadast_client.setFont(font)
        self.tab_cadast_client.setObjectName("tab_cadast_client")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_cadast_client)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineE_nome_cliente = QtWidgets.QLineEdit(self.tab_cadast_client)
        self.lineE_nome_cliente.setObjectName("lineE_nome_cliente")
        self.gridLayout_4.addWidget(self.lineE_nome_cliente, 0, 1, 1, 1)
        self.table_cliente = QtWidgets.QTableWidget(self.tab_cadast_client)
        self.table_cliente.setMinimumSize(QtCore.QSize(600, 0))
        self.table_cliente.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_cliente.setObjectName("table_cliente")
        self.table_cliente.setColumnCount(3)
        self.table_cliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(2, item)
        self.gridLayout_4.addWidget(self.table_cliente, 4, 0, 1, 3)
        self.pushB_cadastrar_cliente = QtWidgets.QPushButton(self.tab_cadast_client)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushB_cadastrar_cliente.setFont(font)
        self.pushB_cadastrar_cliente.setObjectName("pushB_cadastrar_cliente")
        self.gridLayout_4.addWidget(self.pushB_cadastrar_cliente, 0, 2, 2, 1)
        self.lineE_idade_cliente = QtWidgets.QLineEdit(self.tab_cadast_client)
        self.lineE_idade_cliente.setObjectName("lineE_idade_cliente")
        self.gridLayout_4.addWidget(self.lineE_idade_cliente, 1, 1, 1, 1)
        self.label_nome_cliente = QtWidgets.QLabel(self.tab_cadast_client)
        self.label_nome_cliente.setObjectName("label_nome_cliente")
        self.gridLayout_4.addWidget(self.label_nome_cliente, 0, 0, 1, 1)
        self.label_idade_clinete = QtWidgets.QLabel(self.tab_cadast_client)
        self.label_idade_clinete.setObjectName("label_idade_clinete")
        self.gridLayout_4.addWidget(self.label_idade_clinete, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.tab_cadast_client)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushB_edit_cliente = QtWidgets.QPushButton(self.frame)
        self.pushB_edit_cliente.setMinimumSize(QtCore.QSize(0, 30))
        self.pushB_edit_cliente.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushB_edit_cliente.setFont(font)
        self.pushB_edit_cliente.setObjectName("pushB_edit_cliente")
        self.horizontalLayout.addWidget(self.pushB_edit_cliente)
        self.pushB_delet_cliente = QtWidgets.QPushButton(self.frame)
        self.pushB_delet_cliente.setMinimumSize(QtCore.QSize(0, 30))
        self.pushB_delet_cliente.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushB_delet_cliente.setFont(font)
        self.pushB_delet_cliente.setObjectName("pushB_delet_cliente")
        self.horizontalLayout.addWidget(self.pushB_delet_cliente)
        self.gridLayout_4.addWidget(self.frame, 2, 1, 1, 1)
        self.tab_center.addTab(self.tab_cadast_client, "")
        self.tab_statistic = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Noto Sans Lao")
        font.setPointSize(12)
        self.tab_statistic.setFont(font)
        self.tab_statistic.setObjectName("tab_statistic")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_statistic)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.tab_statistic)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_title_qt3 = QtWidgets.QLabel(self.frame_3)
        self.label_title_qt3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_qt3.setObjectName("label_title_qt3")
        self.gridLayout_8.addWidget(self.label_title_qt3, 0, 0, 1, 1)
        self.label_title_qt4 = QtWidgets.QLabel(self.frame_3)
        self.label_title_qt4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_qt4.setObjectName("label_title_qt4")
        self.gridLayout_8.addWidget(self.label_title_qt4, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_3, 2, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.tab_statistic)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_title_qt1 = QtWidgets.QLabel(self.frame_2)
        self.label_title_qt1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_qt1.setObjectName("label_title_qt1")
        self.gridLayout_6.addWidget(self.label_title_qt1, 0, 0, 1, 1)
        self.label_title_qt2 = QtWidgets.QLabel(self.frame_2)
        self.label_title_qt2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_qt2.setObjectName("label_title_qt2")
        self.gridLayout_6.addWidget(self.label_title_qt2, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 2)
        self.label_qt3 = QtWidgets.QLabel(self.tab_statistic)
        self.label_qt3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qt3.setObjectName("label_qt3")
        self.gridLayout_5.addWidget(self.label_qt3, 3, 0, 1, 1)
        self.label_qt2 = QtWidgets.QLabel(self.tab_statistic)
        self.label_qt2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qt2.setObjectName("label_qt2")
        self.gridLayout_5.addWidget(self.label_qt2, 1, 1, 1, 1)
        self.label_qt4 = QtWidgets.QLabel(self.tab_statistic)
        self.label_qt4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qt4.setObjectName("label_qt4")
        self.gridLayout_5.addWidget(self.label_qt4, 3, 1, 1, 1)
        self.label_qt1 = QtWidgets.QLabel(self.tab_statistic)
        self.label_qt1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qt1.setObjectName("label_qt1")
        self.gridLayout_5.addWidget(self.label_qt1, 1, 0, 1, 1)
        self.label_qt5 = QtWidgets.QLabel(self.tab_statistic)
        self.label_qt5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qt5.setObjectName("label_qt5")
        self.gridLayout_5.addWidget(self.label_qt5, 5, 0, 1, 2)
        self.frame_4 = QtWidgets.QFrame(self.tab_statistic)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_title_qt5 = QtWidgets.QLabel(self.frame_4)
        self.label_title_qt5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_qt5.setObjectName("label_title_qt5")
        self.gridLayout_7.addWidget(self.label_title_qt5, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_4, 4, 0, 1, 2)
        self.tab_center.addTab(self.tab_statistic, "")
        self.gridLayout.addWidget(self.tab_center, 1, 1, 1, 2)
        self.label_TITLE = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Lao")
        font.setPointSize(18)
        self.label_TITLE.setFont(font)
        self.label_TITLE.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TITLE.setObjectName("label_TITLE")
        self.gridLayout.addWidget(self.label_TITLE, 0, 1, 1, 2)
        self.label_hoje = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_hoje.setFont(font)
        self.label_hoje.setObjectName("label_hoje")
        self.gridLayout.addWidget(self.label_hoje, 2, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_center.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table_center.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cliente"))
        item = self.table_center.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Produto"))
        item = self.table_center.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Peso"))
        item = self.table_center.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Valor"))
        item = self.table_center.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Data"))
        self.label_img.setText(_translate("MainWindow", "Imagem"))
        self.label_client.setText(_translate("MainWindow", "Cliente :"))
        self.label_weight_2.setText(_translate("MainWindow", "Peso :"))
        self.label_produt_preco.setText(_translate("MainWindow", "Preço (Kg) : "))
        self.label_produt.setText(_translate("MainWindow", "Produto : "))
        self.pB_add_car.setText(_translate("MainWindow", "ADICIONAR AO CARRINHO"))
        self.label_kg.setText(_translate("MainWindow", "Kg"))
        self.pushB_comprar.setText(_translate("MainWindow", "COMPRAR"))
        self.pushB_limpar.setText(_translate("MainWindow", "LIMPAR"))
        self.pushB_apagar.setText(_translate("MainWindow", "APAGAR"))
        self.tab_center.setTabText(self.tab_center.indexOf(self.tab_vendas), _translate("MainWindow", "Vendas"))
        self.label_consult_nome.setText(_translate("MainWindow", "Nome:"))
        self.label.setText(_translate("MainWindow", "CONSULTAR VENDAS"))
        self.label_consult_data.setText(_translate("MainWindow", "Data: "))
        self.pushB_consultar.setText(_translate("MainWindow", "CONSULTAR"))
        item = self.table_cunsulta.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id_venda"))
        item = self.table_cunsulta.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "cliente"))
        item = self.table_cunsulta.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "produto"))
        item = self.table_cunsulta.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "peso"))
        item = self.table_cunsulta.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "valor"))
        item = self.table_cunsulta.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "data"))
        self.tab_center.setTabText(self.tab_center.indexOf(self.tab_consult_vendas), _translate("MainWindow", "Consultar vendas"))
        item = self.table_cliente.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id_cliente"))
        item = self.table_cliente.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "nome_clinete"))
        item = self.table_cliente.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "idade_cliente"))
        self.pushB_cadastrar_cliente.setText(_translate("MainWindow", "CADASTRAR"))
        self.label_nome_cliente.setText(_translate("MainWindow", "Nome: "))
        self.label_idade_clinete.setText(_translate("MainWindow", "Idade: "))
        self.pushB_edit_cliente.setText(_translate("MainWindow", "EDITAR CLIENTE"))
        self.pushB_delet_cliente.setText(_translate("MainWindow", "DELETAR CLIENTE"))
        self.tab_center.setTabText(self.tab_center.indexOf(self.tab_cadast_client), _translate("MainWindow", "Cadastrar cliente"))
        self.label_title_qt3.setText(_translate("MainWindow", "title_3"))
        self.label_title_qt4.setText(_translate("MainWindow", "title_4"))
        self.label_title_qt1.setText(_translate("MainWindow", "title_1"))
        self.label_title_qt2.setText(_translate("MainWindow", "title_2"))
        self.label_qt3.setText(_translate("MainWindow", "qt3"))
        self.label_qt2.setText(_translate("MainWindow", "qt2"))
        self.label_qt4.setText(_translate("MainWindow", "qt4"))
        self.label_qt1.setText(_translate("MainWindow", "qt1"))
        self.label_qt5.setText(_translate("MainWindow", "qt5"))
        self.label_title_qt5.setText(_translate("MainWindow", "title_5"))
        self.tab_center.setTabText(self.tab_center.indexOf(self.tab_statistic), _translate("MainWindow", "Estatísticas"))
        self.label_TITLE.setText(_translate("MainWindow", "SISTEMA DE VENDAS"))
        self.label_hoje.setText(_translate("MainWindow", "Hoje"))
