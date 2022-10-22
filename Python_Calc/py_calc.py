from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Calculadora_Qt(object):
    def setupUi(self, Calculadora_Qt):
        if not Calculadora_Qt.objectName():
            Calculadora_Qt.setObjectName(u"Calculadora_Qt")
        Calculadora_Qt.resize(400, 450)
        Calculadora_Qt.setMinimumSize(QSize(400, 450))
        Calculadora_Qt.setMaximumSize(QSize(400, 450))
        self.centralwidget = QWidget(Calculadora_Qt)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(400, 450))
        self.centralwidget.setMaximumSize(QSize(400, 450))
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"background-color: #252946;")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_main)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 25))
        self.label.setMaximumSize(QSize(200, 25))
        self.label.setStyleSheet(u"color: rgb(217, 217, 217);")

        self.verticalLayout.addWidget(self.label)

        self.frame_dg = QFrame(self.frame_main)
        self.frame_dg.setObjectName(u"frame_dg")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_dg.sizePolicy().hasHeightForWidth())
        self.frame_dg.setSizePolicy(sizePolicy)
        self.frame_dg.setMinimumSize(QSize(380, 80))
        self.frame_dg.setMaximumSize(QSize(380, 80))
        self.frame_dg.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_dg.setFrameShape(QFrame.StyledPanel)
        self.frame_dg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_dg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.painel = QLabel(self.frame_dg)
        self.painel.setObjectName(u"painel")
        font = QFont()
        font.setFamily(u"MS Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.painel.setFont(font)
        self.painel.setStyleSheet(u"")
        self.painel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.painel)


        self.verticalLayout.addWidget(self.frame_dg)

        self.frame = QFrame(self.frame_main)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 231, 301))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_9 = QPushButton(self.frame_3)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setGeometry(QRect(150, 10, 60, 60))
        self.btn_9.setMinimumSize(QSize(60, 60))
        self.btn_9.setMaximumSize(QSize(60, 60))
        font1 = QFont()
        font1.setFamily(u"Noto Sans")
        font1.setPointSize(16)
        self.btn_9.setFont(font1)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_8 = QPushButton(self.frame_3)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setGeometry(QRect(80, 10, 60, 60))
        self.btn_8.setMinimumSize(QSize(60, 60))
        self.btn_8.setMaximumSize(QSize(60, 60))
        self.btn_8.setFont(font1)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_8.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_7 = QPushButton(self.frame_3)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setGeometry(QRect(10, 10, 60, 60))
        self.btn_7.setMinimumSize(QSize(0, 60))
        self.btn_7.setMaximumSize(QSize(60, 60))
        self.btn_7.setFont(font1)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"	\n"
"}\n"
"\n"
"")
        self.btn_4 = QPushButton(self.frame_3)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setGeometry(QRect(10, 80, 60, 60))
        self.btn_4.setMinimumSize(QSize(60, 60))
        self.btn_4.setMaximumSize(QSize(60, 60))
        self.btn_4.setFont(font1)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_5 = QPushButton(self.frame_3)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setGeometry(QRect(80, 80, 60, 60))
        self.btn_5.setMinimumSize(QSize(60, 60))
        self.btn_5.setMaximumSize(QSize(60, 60))
        self.btn_5.setFont(font1)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_6 = QPushButton(self.frame_3)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setGeometry(QRect(150, 80, 60, 60))
        self.btn_6.setMinimumSize(QSize(60, 60))
        self.btn_6.setMaximumSize(QSize(60, 60))
        self.btn_6.setFont(font1)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_6.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_1 = QPushButton(self.frame_3)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(10, 148, 60, 60))
        self.btn_1.setMinimumSize(QSize(60, 60))
        self.btn_1.setMaximumSize(QSize(60, 60))
        self.btn_1.setFont(font1)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_1.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_2 = QPushButton(self.frame_3)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setGeometry(QRect(80, 148, 60, 60))
        self.btn_2.setMinimumSize(QSize(60, 60))
        self.btn_2.setMaximumSize(QSize(60, 60))
        self.btn_2.setFont(font1)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_3 = QPushButton(self.frame_3)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setGeometry(QRect(150, 148, 60, 60))
        self.btn_3.setMinimumSize(QSize(60, 60))
        self.btn_3.setMaximumSize(QSize(60, 60))
        self.btn_3.setFont(font1)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_0 = QPushButton(self.frame_3)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setGeometry(QRect(10, 220, 130, 60))
        self.btn_0.setMinimumSize(QSize(130, 60))
        self.btn_0.setMaximumSize(QSize(130, 60))
        self.btn_0.setFont(font1)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_0.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_ponto = QPushButton(self.frame_3)
        self.btn_ponto.setObjectName(u"btn_ponto")
        self.btn_ponto.setGeometry(QRect(150, 220, 60, 60))
        self.btn_ponto.setMinimumSize(QSize(60, 60))
        self.btn_ponto.setMaximumSize(QSize(60, 60))
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_ponto.setFont(font2)
        self.btn_ponto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ponto.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(230, 0, 151, 301))
        self.btn_ce = QPushButton(self.widget)
        self.btn_ce.setObjectName(u"btn_ce")
        self.btn_ce.setGeometry(QRect(10, 10, 60, 60))
        self.btn_ce.setMinimumSize(QSize(60, 60))
        self.btn_ce.setMaximumSize(QSize(60, 60))
        self.btn_ce.setFont(font2)
        self.btn_ce.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ce.setStyleSheet(u"QPushButton {\n"
"    background-color: #519af4 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_c = QPushButton(self.widget)
        self.btn_c.setObjectName(u"btn_c")
        self.btn_c.setGeometry(QRect(80, 10, 60, 60))
        self.btn_c.setMinimumSize(QSize(60, 60))
        self.btn_c.setMaximumSize(QSize(60, 60))
        self.btn_c.setFont(font2)
        self.btn_c.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_c.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #f46a51 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_multiplica = QPushButton(self.widget)
        self.btn_multiplica.setObjectName(u"btn_multiplica")
        self.btn_multiplica.setGeometry(QRect(80, 80, 60, 60))
        self.btn_multiplica.setMinimumSize(QSize(60, 60))
        self.btn_multiplica.setMaximumSize(QSize(60, 60))
        self.btn_multiplica.setFont(font2)
        self.btn_multiplica.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_multiplica.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_dividir = QPushButton(self.widget)
        self.btn_dividir.setObjectName(u"btn_dividir")
        self.btn_dividir.setGeometry(QRect(10, 80, 60, 60))
        self.btn_dividir.setMinimumSize(QSize(60, 60))
        self.btn_dividir.setMaximumSize(QSize(60, 60))
        self.btn_dividir.setFont(font2)
        self.btn_dividir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dividir.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_subri = QPushButton(self.widget)
        self.btn_subri.setObjectName(u"btn_subri")
        self.btn_subri.setGeometry(QRect(10, 150, 60, 60))
        self.btn_subri.setMinimumSize(QSize(60, 60))
        self.btn_subri.setMaximumSize(QSize(60, 60))
        font3 = QFont()
        font3.setFamily(u"Noto Sans")
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_subri.setFont(font3)
        self.btn_subri.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_subri.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e7e2 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_soma = QPushButton(self.widget)
        self.btn_soma.setObjectName(u"btn_soma")
        self.btn_soma.setGeometry(QRect(80, 150, 60, 130))
        self.btn_soma.setMinimumSize(QSize(60, 130))
        self.btn_soma.setMaximumSize(QSize(60, 130))
        font4 = QFont()
        font4.setFamily(u"Noto Sans")
        font4.setPointSize(20)
        self.btn_soma.setFont(font4)
        self.btn_soma.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_soma.setStyleSheet(u"QPushButton {\n"
"    background-color: #51f469 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")
        self.btn_igual = QPushButton(self.widget)
        self.btn_igual.setObjectName(u"btn_igual")
        self.btn_igual.setGeometry(QRect(10, 220, 60, 60))
        self.btn_igual.setMinimumSize(QSize(60, 60))
        self.btn_igual.setMaximumSize(QSize(60, 60))
        self.btn_igual.setFont(font3)
        self.btn_igual.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_igual.setStyleSheet(u"QPushButton {\n"
"    background-color: #e8f451 ;\n"
"    border-style: inset;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(193, 193, 193);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.frame_main)

        Calculadora_Qt.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculadora_Qt)

        QMetaObject.connectSlotsByName(Calculadora_Qt)
    # setupUi

    def retranslateUi(self, Calculadora_Qt):
        Calculadora_Qt.setWindowTitle(QCoreApplication.translate("Calculadora_Qt", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Calculadora_Qt", u"OKOSTA_ :: CALCULADORA", None))
        self.painel.setText(QCoreApplication.translate("Calculadora_Qt", u"0", None))
        self.btn_9.setText(QCoreApplication.translate("Calculadora_Qt", u"9", None))
        self.btn_8.setText(QCoreApplication.translate("Calculadora_Qt", u"8", None))
        self.btn_7.setText(QCoreApplication.translate("Calculadora_Qt", u"7", None))
        self.btn_4.setText(QCoreApplication.translate("Calculadora_Qt", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("Calculadora_Qt", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("Calculadora_Qt", u"6", None))
        self.btn_1.setText(QCoreApplication.translate("Calculadora_Qt", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("Calculadora_Qt", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("Calculadora_Qt", u"3", None))
        self.btn_0.setText(QCoreApplication.translate("Calculadora_Qt", u"0", None))
        self.btn_ponto.setText(QCoreApplication.translate("Calculadora_Qt", u".", None))
        self.btn_ce.setText(QCoreApplication.translate("Calculadora_Qt", u"CE", None))
        self.btn_c.setText(QCoreApplication.translate("Calculadora_Qt", u"AC", None))
        self.btn_multiplica.setText(QCoreApplication.translate("Calculadora_Qt", u"*", None))
        self.btn_dividir.setText(QCoreApplication.translate("Calculadora_Qt", u"/", None))
        self.btn_subri.setText(QCoreApplication.translate("Calculadora_Qt", u"-", None))
        self.btn_soma.setText(QCoreApplication.translate("Calculadora_Qt", u"+", None))
        self.btn_igual.setText(QCoreApplication.translate("Calculadora_Qt", u"=", None))
    # retranslateUi

