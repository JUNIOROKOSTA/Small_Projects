from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 400)
        MainWindow.setMinimumSize(QtCore.QSize(660, 400))
        MainWindow.setMaximumSize(QtCore.QSize(660, 400))
        MainWindow.setStyleSheet("background-color: rgb(220, 220, 227);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.483318, y1:0.182, x2:0.472, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_2.setStyleSheet("background-color: rgba(61, 61, 61,10);\n"
"color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Cooper Std Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Cooper Std Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgba(150, 150, 150,30);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pedra_btn = QtWidgets.QPushButton(self.frame_3)
        self.pedra_btn.setMinimumSize(QtCore.QSize(220, 220))
        self.pedra_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pedra_btn.setMouseTracking(False)
        self.pedra_btn.setTabletTracking(False)
        self.pedra_btn.setStyleSheet("#pedra_btn\n"
"{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    background-image: url(:/pedra_img/pedra.png);\n"
"    background-repeat: no_repeat;\n"
"    background-position: center;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"#pedra_btn:hover\n"
"{\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(241, 255, 0, 255), stop:0.232955 rgba(255, 255, 7, 210), stop:0.4 rgba(255, 255, 0, 255), stop:0.89548 rgba(252, 255, 0, 255), stop:1 rgba(255, 255, 0, 0));\n"
"    border: none;\n"
"}\n"
"\n"
"#pedra_btn:pressed\n"
"{\n"
"    background-image: url(:/pedra_img/pedra_sel.png);\n"
"}")
        self.pedra_btn.setText("")
        self.pedra_btn.setObjectName("pedra_btn")
        self.horizontalLayout_2.addWidget(self.pedra_btn)
        self.papel_btn = QtWidgets.QPushButton(self.frame_3)
        self.papel_btn.setMinimumSize(QtCore.QSize(220, 220))
        self.papel_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.papel_btn.setStyleSheet("#papel_btn\n"
"{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    background-image: url(:/papel_img/papel.png);\n"
"    background-repeat: no_repeat;\n"
"    background-position: center;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"#papel_btn:hover\n"
"{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 255, 180, 255), stop:0.232955 rgba(0, 255, 191, 255), stop:0.403409 rgba(0, 255, 180, 255), stop:0.89548 rgba(0, 255, 223, 255), stop:1 rgba(255, 255, 0, 0));\n"
"border: none;\n"
"}\n"
"\n"
"#papel_btn:pressed\n"
"{\n"
"background-image: url(:/papel_img/papel_sel.png);\n"
"}")
        self.papel_btn.setText("")
        self.papel_btn.setObjectName("papel_btn")
        self.horizontalLayout_2.addWidget(self.papel_btn)
        self.tesoura_btn = QtWidgets.QPushButton(self.frame_3)
        self.tesoura_btn.setMinimumSize(QtCore.QSize(220, 220))
        self.tesoura_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tesoura_btn.setStyleSheet("#tesoura_btn\n"
"{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    background-image: url(:/tesoura_img/tesoura.png);\n"
"    background-repeat: no_repeat;\n"
"    background-position: center;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"#tesoura_btn:hover\n"
"{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(241, 0, 255, 255), stop:0.232955 rgba(255, 0, 248, 255), stop:0.403409 rgba(241, 0, 255, 255), stop:0.89548 rgba(246, 158, 255, 255), stop:1 rgba(255, 255, 0, 0));\n"
"border: none;\n"
"}\n"
"\n"
"#tesoura_btn:pressed\n"
"{\n"
"background-image: url(:/tesoura_img/tesoura_sel.png);\n"
"}")
        self.tesoura_btn.setText("")
        self.tesoura_btn.setObjectName("tesoura_btn")
        self.horizontalLayout_2.addWidget(self.tesoura_btn)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_4.setStyleSheet("background-color: rgba(150, 150, 150,60);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.output_display_2 = QtWidgets.QLabel(self.frame_4)
        self.output_display_2.setMinimumSize(QtCore.QSize(320, 88))
        self.output_display_2.setMaximumSize(QtCore.QSize(232, 88))
        font = QtGui.QFont()
        font.setFamily("Cooper Std Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_display_2.setFont(font)
        self.output_display_2.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.output_display_2.setScaledContents(False)
        self.output_display_2.setAlignment(QtCore.Qt.AlignCenter)
        self.output_display_2.setWordWrap(True)
        self.output_display_2.setOpenExternalLinks(True)
        self.output_display_2.setObjectName("output_display_2")
        self.horizontalLayout.addWidget(self.output_display_2, 0, QtCore.Qt.AlignHCenter)
        self.output_display = QtWidgets.QLabel(self.frame_4)
        self.output_display.setMinimumSize(QtCore.QSize(320, 88))
        font = QtGui.QFont()
        font.setFamily("Cooper Std Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.output_display.setFont(font)
        self.output_display.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.output_display.setScaledContents(False)
        self.output_display.setAlignment(QtCore.Qt.AlignCenter)
        self.output_display.setWordWrap(True)
        self.output_display.setOpenExternalLinks(True)
        self.output_display.setObjectName("output_display")
        self.horizontalLayout.addWidget(self.output_display, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Jokenpô"))
        self.label_2.setText(_translate("MainWindow", "Escolha sua \"mão\""))
        self.output_display_2.setText(_translate("MainWindow", "Humano vs Maquina"))
        self.output_display.setText(_translate("MainWindow", "Humano vs Maquina"))
from Jokenpo import file_img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
