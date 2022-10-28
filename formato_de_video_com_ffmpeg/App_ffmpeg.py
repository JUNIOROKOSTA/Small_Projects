import sys
from janela import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from ffmpegvideo import convertvideo

# pyuic5 -x janela.ui -o janela.py


class App(QMainWindow, Ui_Qt_Janela):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle('FFmegVideo')

        self.setup()

        self.video = ''
        self.formato = ''

        self.pb_buscar_path.clicked.connect(self.load_img)
        self.pb_converter.clicked.connect(self.converter_formato)
        self.pb_play.clicked.connect(self.mediaPlayer.play)
        self.pb_pause.clicked.connect(self.mediaPlayer.pause)
        self.pb_stop.clicked.connect(self.mediaPlayer.stop)

    def setup(self):
        self.videoOutput = self.makeVideoWidget()
        self.mediaPlayer = self.makeMediaPlayer()

    def makeVideoWidget(self):
        videoOutput = QVideoWidget(self)
        vbox = QVBoxLayout()
        vbox.addWidget(videoOutput)
        self.videoWidget.setLayout(vbox)

        return videoOutput

    def makeMediaPlayer(self):
        mediaPlayer = QMediaPlayer(self)
        mediaPlayer.setVideoOutput(self.videoOutput)
        return mediaPlayer

    def load_img(self):
        self.video, xx = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Escolher o VÍDEO',
        )
        self.le_caminho.setText(self.video)

        self.mediaPlayer.setMedia(QMediaContent(QUrl(self.video)))
        self.mediaPlayer.play()
        self.mediaPlayer.pause()

    def converter_formato(self):
        self.formato = '.' + self.le_formato.text()
        if self.video == '' or self.formato == '':
            return
        confirme = convertvideo(self.video, self.formato)

        self.media

        if confirme == 'ok':
            self.le_caminho.setText('')
            self.le_formato.setText('')


if __name__ == '__main__':
    aplication = QApplication(sys.argv)
    app = App()
    app.show()
    try:
        sys.exit(aplication.exec_())
    except SystemError:
        print('Closing window...')
