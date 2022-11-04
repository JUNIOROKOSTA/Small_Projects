# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 807)
        MainWindow.setStyleSheet("background-color: rgb(0, 157, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.f_tabela = QtWidgets.QFrame(self.centralwidget)
        self.f_tabela.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.f_tabela.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_tabela.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_tabela.setObjectName("f_tabela")
        self.gridLayout = QtWidgets.QGridLayout(self.f_tabela)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_titulo2 = QtWidgets.QLabel(self.f_tabela)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_titulo2.setFont(font)
        self.lb_titulo2.setStyleSheet("color: rgb(0, 149, 0);")
        self.lb_titulo2.setObjectName("lb_titulo2")
        self.gridLayout.addWidget(self.lb_titulo2, 0, 0, 1, 1)
        self.pb_resultado = QtWidgets.QPushButton(self.f_tabela)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb_resultado.setFont(font)
        self.pb_resultado.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_resultado.setMouseTracking(False)
        self.pb_resultado.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 85, 0);\n"
"    \n"
"    color: rgb(255, 255, 127);\n"
"    \n"
"    border: 2px solid;\n"
"    \n"
"    border-color:  rgb(5, 104, 4);\n"
"    \n"
"    border-radius: 9px;\n"
"\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 85, 0);\n"
"    \n"
"    color: rgb(255, 255, 127);\n"
"    \n"
"    border: 2px solid;\n"
"    \n"
"    border-color:  rgb(248, 252, 5);\n"
"    \n"
"    border-radius: 9px;\n"
"\n"
"    padding: 10px;\n"
"}")
        self.pb_resultado.setObjectName("pb_resultado")
        self.gridLayout.addWidget(self.pb_resultado, 2, 0, 1, 1)
        self.tabela = QtWidgets.QTableWidget(self.f_tabela)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabela.setFont(font)
        self.tabela.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.tabela.setObjectName("tabela")
        self.tabela.setColumnCount(6)
        self.tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabela.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabela.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabela.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabela.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabela.setHorizontalHeaderItem(5, item)
        self.tabela.horizontalHeader().setCascadingSectionResizes(True)
        self.tabela.horizontalHeader().setDefaultSectionSize(150)
        self.gridLayout.addWidget(self.tabela, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.f_tabela, 2, 0, 1, 4)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(280, 280))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_imagem = QtWidgets.QLabel(self.frame)
        self.label_imagem.setObjectName("label_imagem")
        self.horizontalLayout.addWidget(self.label_imagem)
        self.gridLayout_3.addWidget(self.frame, 1, 3, 1, 1)
        self.lb_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lb_titulo.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_titulo.setFont(font)
        self.lb_titulo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lb_titulo.setStyleSheet("color: rgb(255, 255, 127);")
        self.lb_titulo.setObjectName("lb_titulo")
        self.gridLayout_3.addWidget(self.lb_titulo, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.f_sistema = QtWidgets.QFrame(self.centralwidget)
        self.f_sistema.setMaximumSize(QtCore.QSize(16777215, 280))
        self.f_sistema.setStyleSheet("background-color: rgb(0, 157, 0);")
        self.f_sistema.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_sistema.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_sistema.setObjectName("f_sistema")
        self.formLayout = QtWidgets.QFormLayout(self.f_sistema)
        self.formLayout.setObjectName("formLayout")
        self.label_concurso = QtWidgets.QLabel(self.f_sistema)
        self.label_concurso.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_concurso.setFont(font)
        self.label_concurso.setStyleSheet("color: rgb(255, 255, 127);")
        self.label_concurso.setObjectName("label_concurso")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_concurso)
        self.le_Concurso = QtWidgets.QLineEdit(self.f_sistema)
        self.le_Concurso.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_Concurso.setFont(font)
        self.le_Concurso.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.le_Concurso.setText("")
        self.le_Concurso.setAlignment(QtCore.Qt.AlignCenter)
        self.le_Concurso.setPlaceholderText("Concurso")
        self.le_Concurso.setObjectName("le_Concurso")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_Concurso)
        self.label_data = QtWidgets.QLabel(self.f_sistema)
        self.label_data.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_data.setFont(font)
        self.label_data.setStyleSheet("color: rgb(255, 255, 127);")
        self.label_data.setObjectName("label_data")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_data)
        self.le_Data = QtWidgets.QLineEdit(self.f_sistema)
        self.le_Data.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_Data.setFont(font)
        self.le_Data.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.le_Data.setText("")
        self.le_Data.setAlignment(QtCore.Qt.AlignCenter)
        self.le_Data.setPlaceholderText("Data")
        self.le_Data.setObjectName("le_Data")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_Data)
        self.lb_semTitulo = QtWidgets.QLabel(self.f_sistema)
        self.lb_semTitulo.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_semTitulo.setFont(font)
        self.lb_semTitulo.setStyleSheet("color: rgb(255, 255, 127);")
        self.lb_semTitulo.setObjectName("lb_semTitulo")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lb_semTitulo)
        self.le_aposta_sorte = QtWidgets.QLineEdit(self.f_sistema)
        self.le_aposta_sorte.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_aposta_sorte.setFont(font)
        self.le_aposta_sorte.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.le_aposta_sorte.setText("")
        self.le_aposta_sorte.setAlignment(QtCore.Qt.AlignCenter)
        self.le_aposta_sorte.setPlaceholderText("!!! Sorte de Deus !!!")
        self.le_aposta_sorte.setObjectName("le_aposta_sorte")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.le_aposta_sorte)
        self.pb_gerar_sorte = QtWidgets.QPushButton(self.f_sistema)
        self.pb_gerar_sorte.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_gerar_sorte.setFont(font)
        self.pb_gerar_sorte.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_gerar_sorte.setMouseTracking(False)
        self.pb_gerar_sorte.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 85, 0);\n"
"    \n"
"    color: rgb(255, 255, 127);\n"
"    \n"
"    border: 2px solid;\n"
"    \n"
"    border-color:  rgb(5, 104, 4);\n"
"    \n"
"    border-radius: 9px;\n"
"\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 85, 0);\n"
"    \n"
"    color: rgb(255, 255, 127);\n"
"    \n"
"    border: 2px solid;\n"
"    \n"
"    border-color:  rgb(248, 252, 5);\n"
"    \n"
"    border-radius: 9px;\n"
"\n"
"    padding: 10px;\n"
"}")
        self.pb_gerar_sorte.setObjectName("pb_gerar_sorte")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pb_gerar_sorte)
        self.lb_msn = QtWidgets.QLabel(self.f_sistema)
        self.lb_msn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_msn.setFont(font)
        self.lb_msn.setStyleSheet("color: rgb(255, 255, 127);")
        self.lb_msn.setObjectName("lb_msn")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.lb_msn)
        self.pb_registrar_sorte = QtWidgets.QPushButton(self.f_sistema)
        self.pb_registrar_sorte.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_registrar_sorte.setFont(font)
        self.pb_registrar_sorte.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_registrar_sorte.setMouseTracking(False)
        self.pb_registrar_sorte.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 85, 0);\n"
"    \n"
"    color: rgb(255, 255, 127);\n"
"    \n"
"    border: 2px solid;\n"
"    \n"
"    border-color:  rgb(5, 104, 4);\n"
"    \n"
"    border-radius: 9px;\n"
"\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 85, 0);\n"
"    \n"
"    color: rgb(255, 255, 127);\n"
"    \n"
"    border: 2px solid;\n"
"    \n"
"    border-color:  rgb(248, 252, 5);\n"
"    \n"
"    border-radius: 9px;\n"
"\n"
"    padding: 10px;\n"
"}")
        self.pb_registrar_sorte.setObjectName("pb_registrar_sorte")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pb_registrar_sorte)
        self.gridLayout_3.addWidget(self.f_sistema, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabela, self.pb_resultado)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_titulo2.setText(_translate("MainWindow", "Tabela com Registros"))
        self.pb_resultado.setText(_translate("MainWindow", "Buscar Resultados"))
        item = self.tabela.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Concurso"))
        item = self.tabela.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Aposta"))
        item = self.tabela.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data Aposta"))
        item = self.tabela.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Num_Resultado"))
        item = self.tabela.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Valor Premio"))
        item = self.tabela.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Acertos"))
        self.label_imagem.setText(_translate("MainWindow", "imagem"))
        self.lb_titulo.setText(_translate("MainWindow", "Mega-Sena da Sorte!"))
        self.label_concurso.setText(_translate("MainWindow", "Concurso:"))
        self.label_data.setText(_translate("MainWindow", "Data:"))
        self.lb_semTitulo.setText(_translate("MainWindow", "GERAR APOSTA:"))
        self.pb_gerar_sorte.setText(_translate("MainWindow", "Gerar Sorte"))
        self.lb_msn.setText(_translate("MainWindow", "..."))
        self.pb_registrar_sorte.setText(_translate("MainWindow", "Registrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
