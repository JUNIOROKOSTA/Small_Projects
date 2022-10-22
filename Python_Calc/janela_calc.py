from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculadora_Qt(object):
    def setupUi(self, Calculadora_Qt):
        Calculadora_Qt.setObjectName("Calculadora_Qt")
        Calculadora_Qt.resize(400, 450)
        Calculadora_Qt.setMinimumSize(QtCore.QSize(400, 450))
        Calculadora_Qt.setMaximumSize(QtCore.QSize(400, 450))
        self.centralwidget = QtWidgets.QWidget(Calculadora_Qt)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 450))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 450))
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("background-color: #252946;")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_main)
        self.label.setMinimumSize(QtCore.QSize(200, 25))
        self.label.setMaximumSize(QtCore.QSize(200, 25))
        self.label.setStyleSheet("color: rgb(217, 217, 217);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_dg = QtWidgets.QFrame(self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_dg.sizePolicy().hasHeightForWidth())
        self.frame_dg.setSizePolicy(sizePolicy)
        self.frame_dg.setMinimumSize(QtCore.QSize(380, 80))
        self.frame_dg.setMaximumSize(QtCore.QSize(380, 80))
        self.frame_dg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_dg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dg.setObjectName("frame_dg")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_dg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.painel = QtWidgets.QLabel(self.frame_dg)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.painel.setFont(font)
        self.painel.setStyleSheet("")
        self.painel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.painel.setObjectName("painel")
        self.verticalLayout_2.addWidget(self.painel)
        self.verticalLayout.addWidget(self.frame_dg)
        self.frame = QtWidgets.QFrame(self.frame_main)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 231, 301))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btn_9 = QtWidgets.QPushButton(self.frame_3)
        self.btn_9.setGeometry(QtCore.QRect(150, 10, 60, 60))
        self.btn_9.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_9.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.btn_9.setFont(font)
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_9.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.frame_3)
        self.btn_8.setGeometry(QtCore.QRect(80, 10, 60, 60))
        self.btn_8.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_8.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.btn_8.setFont(font)
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_8.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_8.setObjectName("btn_8")
        self.btn_7 = QtWidgets.QPushButton(self.frame_3)
        self.btn_7.setGeometry(QtCore.QRect(10, 10, 60, 60))
        self.btn_7.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_7.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.btn_7.setFont(font)
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_7.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "    \n"
        "}\n"
        "\n"
        "")
        self.btn_7.setObjectName("btn_7")
        self.btn_4 = QtWidgets.QPushButton(self.frame_3)
        self.btn_4.setGeometry(QtCore.QRect(10, 80, 60, 60))
        self.btn_4.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_4.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.btn_4.setFont(font)
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_4.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.frame_3)
        self.btn_5.setGeometry(QtCore.QRect(80, 80, 60, 60))
        self.btn_5.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_5.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.btn_5.setFont(font)
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_5.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.frame_3)
        self.btn_6.setGeometry(QtCore.QRect(150, 80, 60, 60))
        self.btn_6.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_6.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.btn_6.setFont(font)
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_6.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_6.setObjectName("btn_6")
        self.btn_1 = QtWidgets.QPushButton(self.frame_3)
        self.btn_1.setGeometry(QtCore.QRect(10, 148, 60, 60))
        self.btn_1.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_1.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.btn_1.setFont(font)
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.frame_3)
        self.btn_2.setGeometry(QtCore.QRect(80, 148, 60, 60))
        self.btn_2.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_2.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.btn_2.setFont(font)
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.frame_3)
        self.btn_3.setGeometry(QtCore.QRect(150, 148, 60, 60))
        self.btn_3.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_3.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.btn_3.setFont(font)
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_3.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_3.setObjectName("btn_3")
        self.btn_0 = QtWidgets.QPushButton(self.frame_3)
        self.btn_0.setGeometry(QtCore.QRect(10, 220, 130, 60))
        self.btn_0.setMinimumSize(QtCore.QSize(130, 60))
        self.btn_0.setMaximumSize(QtCore.QSize(130, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.btn_0.setFont(font)
        self.btn_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_0.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_0.setObjectName("btn_0")
        self.btn_ponto = QtWidgets.QPushButton(self.frame_3)
        self.btn_ponto.setGeometry(QtCore.QRect(150, 220, 60, 60))
        self.btn_ponto.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_ponto.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ponto.setFont(font)
        self.btn_ponto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ponto.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_ponto.setObjectName("btn_ponto")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(230, 0, 151, 301))
        self.widget.setObjectName("widget")
        self.btn_ce = QtWidgets.QPushButton(self.widget)
        self.btn_ce.setGeometry(QtCore.QRect(10, 10, 60, 60))
        self.btn_ce.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_ce.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ce.setFont(font)
        self.btn_ce.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ce.setStyleSheet("QPushButton {\n"
        "    background-color: #519af4 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_ce.setObjectName("btn_ce")
        self.btn_c = QtWidgets.QPushButton(self.widget)
        self.btn_c.setGeometry(QtCore.QRect(80, 10, 60, 60))
        self.btn_c.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_c.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_c.setFont(font)
        self.btn_c.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c.setStyleSheet("\n"
        "QPushButton {\n"
        "    background-color: #f46a51 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_c.setObjectName("btn_c")
        self.btn_multiplica = QtWidgets.QPushButton(self.widget)
        self.btn_multiplica.setGeometry(QtCore.QRect(80, 80, 60, 60))
        self.btn_multiplica.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_multiplica.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_multiplica.setFont(font)
        self.btn_multiplica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_multiplica.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_multiplica.setObjectName("btn_multiplica")
        self.btn_dividir = QtWidgets.QPushButton(self.widget)
        self.btn_dividir.setGeometry(QtCore.QRect(10, 80, 60, 60))
        self.btn_dividir.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_dividir.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dividir.setFont(font)
        self.btn_dividir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_dividir.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_dividir.setObjectName("btn_dividir")
        self.btn_subri = QtWidgets.QPushButton(self.widget)
        self.btn_subri.setGeometry(QtCore.QRect(10, 150, 60, 60))
        self.btn_subri.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_subri.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_subri.setFont(font)
        self.btn_subri.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_subri.setStyleSheet("QPushButton {\n"
        "    background-color: #e6e7e2 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_subri.setObjectName("btn_subri")
        self.btn_soma = QtWidgets.QPushButton(self.widget)
        self.btn_soma.setGeometry(QtCore.QRect(80, 150, 60, 130))
        self.btn_soma.setMinimumSize(QtCore.QSize(60, 130))
        self.btn_soma.setMaximumSize(QtCore.QSize(60, 130))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(20)
        self.btn_soma.setFont(font)
        self.btn_soma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_soma.setStyleSheet("QPushButton {\n"
        "    background-color: #51f469 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_soma.setObjectName("btn_soma")
        self.btn_igual = QtWidgets.QPushButton(self.widget)
        self.btn_igual.setGeometry(QtCore.QRect(10, 220, 60, 60))
        self.btn_igual.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_igual.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_igual.setFont(font)
        self.btn_igual.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_igual.setStyleSheet("QPushButton {\n"
        "    background-color: #e8f451 ;\n"
        "    border-style: inset;\n"
        "    border-width: 6px;\n"
        "    border-radius: 10px;\n"
        "    border-color:rgb(193, 193, 193);\n"
        "}\n"
        "")
        self.btn_igual.setObjectName("btn_igual")
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.frame_main)
        Calculadora_Qt.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculadora_Qt)
        QtCore.QMetaObject.connectSlotsByName(Calculadora_Qt)

    def retranslateUi(self, Calculadora_Qt):
        _translate = QtCore.QCoreApplication.translate
        Calculadora_Qt.setWindowTitle(_translate("Calculadora_Qt", "MainWindow"))
        self.label.setText(_translate("Calculadora_Qt", "OKOSTA_ :: CALCULADORA"))
        self.painel.setText(_translate("Calculadora_Qt", "0"))
        self.btn_9.setText(_translate("Calculadora_Qt", "9"))
        self.btn_8.setText(_translate("Calculadora_Qt", "8"))
        self.btn_7.setText(_translate("Calculadora_Qt", "7"))
        self.btn_4.setText(_translate("Calculadora_Qt", "4"))
        self.btn_5.setText(_translate("Calculadora_Qt", "5"))
        self.btn_6.setText(_translate("Calculadora_Qt", "6"))
        self.btn_1.setText(_translate("Calculadora_Qt", "1"))
        self.btn_2.setText(_translate("Calculadora_Qt", "2"))
        self.btn_3.setText(_translate("Calculadora_Qt", "3"))
        self.btn_0.setText(_translate("Calculadora_Qt", "0"))
        self.btn_ponto.setText(_translate("Calculadora_Qt", "."))
        self.btn_ce.setText(_translate("Calculadora_Qt", "CE"))
        self.btn_c.setText(_translate("Calculadora_Qt", "AC"))
        self.btn_multiplica.setText(_translate("Calculadora_Qt", "*"))
        self.btn_dividir.setText(_translate("Calculadora_Qt", "/"))
        self.btn_subri.setText(_translate("Calculadora_Qt", "-"))
        self.btn_soma.setText(_translate("Calculadora_Qt", "+"))
        self.btn_igual.setText(_translate("Calculadora_Qt", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculadora_Qt = QtWidgets.QMainWindow()
    ui = Ui_Calculadora_Qt()
    ui.setupUi(Calculadora_Qt)
    Calculadora_Qt.show()
    sys.exit(app.exec_())
