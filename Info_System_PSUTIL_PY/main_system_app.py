import sys
import platform
import traceback
import psutil
import shutil
# Usar o * é uma forma errada de importa os pacotes da "biblioteca",
# Verificar quais sãos os medulos que preciso de cada uma delas.
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from windows import Ui_MainWindow
from datetime import datetime
from time import sleep


class WorkerSignals(QObject):

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # metodo de callback para kwargs:
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):

        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class TelManage(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(TelManage, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('System-information')
        self.mini_tela = True  # VARIAVEL AUXILIAR ---> FullScreen
        # Remover a Borda padrão da Janela
        self.setWindowFlag(Qt.FramelessWindowHint)

        QSizeGrip(self.size_grip)

##############################################################################
# Setando botões btn_close, btn_max_mim, btn_hide:
        self.btn_max_mim.clicked.connect(self.fullScreen)
        self.btn_close.clicked.connect(self.close)
        self.btn_hide.clicked.connect(self.showMinimized)
        self.btn_slider_menuBar.clicked.connect(self.sliderMenuBar)

##############################################################################
# Setando botões:
# Setando as telas de dados, criadas usando PySide2.QtWidgets.QStackedWidget .
        self.a1_cpu.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.cpu_ram))

        self.a2_battery.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.battery))

        self.a3_system_Info.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.info_system))

        self.a4_activities.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ativities))

        self.a5_storage.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.storage))

        self.a6_sensors.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.sensors))

        self.a7_networks.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.networks))
##############################################################################

        # ____________________________________________
        # Inicializar os Threads:
        self.threadpool = QThreadPool()
        # ____________________________________________

        # self.painel_battery()
        # self.painel_cpu_ram()
        self.system_info()
        self.processos()
        self.armazenamento()
        self.psutil_threads()
        self.painel_netWorks()


##############################################################################
# Criar as funções utilitarias dos Threads:


    def psutil_threads(self):
        worker = Worker(self.painel_cpu_ram)

        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.process_fn)

        self.threadpool.start(worker)

        battery_worker = Worker(self.painel_battery)
        battery_worker.signals.result.connect(self.print_output)
        battery_worker.signals.finished.connect(self.thread_complete)
        battery_worker.signals.progress.connect(self.process_fn)

        self.threadpool.start(battery_worker)

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("Thread Complete!!!")

    def process_fn(self, n):
        print(f"{n} dane.")


##############################################################################
# Setando evento de tela:

# Evento de Tela cheia:


    def fullScreen(self):  # Metodo => Manipula Tela

        if self.mini_tela:
            self.showFullScreen()  # Metodo : para deixar tela em tamanho FullScreen
            self.mini_tela = False
        else:
            self.showNormal()  # Metodo : para deixar tela em tamanho normal
            self.mini_tela = True

 # Evento de arrastar a tela:
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

# Evento de Mostrar e Esconder a Barra de Menu:

    def sliderMenuBar(self):
        width = self.f_menu_l.width()  # pegando o tamanho corrent da frame da barra-menu

        if width <= 50:  # se for 50 ou menor, aplica novo tamanho de 230
            newWidth = 230
        else:  # se não, aplica novo tamanho de 40
            newWidth = 50

    # Configurando animação da barra de menu:

        self.animater = QPropertyAnimation(self.f_menu_l, b'minimumWidth')
        self.animater.setDuration(350)
        self.animater.setEasingCurve(QEasingCurve.InOutQuart)
        self.animater.setStartValue(width)
        self.animater.setEndValue(newWidth)
        self.animater.start()


##############################################################################

##############################################################################
# Configurando painel da Bateria

    def painel_battery(self, progress_callback):
        while True:
            batt = psutil.sensors_battery()

            if batt is None:
                self.lb_battery_status.setText("O Sistema não possui Bateria")

                self.lb_battery_Carga.setText('0%')
                self.lb_battery_plugado.setText('Não')
                self.lb_battery_Tempo.setText('N/A')

                self.battery_used.rpb_setMaximum(100)
                self.battery_used.rpb_setValue(50)
                self.battery_used.rpb_setBarStyle('Hybrid2')
                self.battery_used.rpb_setLineColor((255, 33, 99))
                self.battery_used.rpb_setTextColor((255, 255, 200))
                self.battery_used.rpb_setInitialPos('South')
                self.battery_used.rpb_setTextFormat('Percentage')
                self.battery_used.rpb_setLineWidth(15)
                self.battery_used.rpb_setPathWidth(15)
                self.battery_used.rpb_setLineCap('RoundCap')
            sleep(1)
##############################################################################

##############################################################################
# Configurando painel CPU e RAM:
    def suport_ram(self, mod):
        totalRam = psutil.virtual_memory()[mod] * 1.0
        totalRam = totalRam / (1024 * 1024 * 1024)
        return totalRam

    def painel_cpu_ram(self, progress_callback):
        while True:
            # configurando dados sobre Memoria RAM:
            total_ram = round(self.suport_ram(0), 4)
            self.lb_ram_total.setText(
                str(f'{total_ram} GB'))
            ram_usada = round(self.suport_ram(3), 4)
            self.lb_ram_usada.setText(
                str(f'{ram_usada} GB'))
            ram_livre = round(self.suport_ram(4), 4)
            self.lb_ram_livre.setText(
                str(f'{ram_livre} GB'))
            ram_disp = round(self.suport_ram(1), 4)
            self.lb_ram_disponivel.setText(
                str(f'{ram_disp} GB'))
            ram_usada_perc = (psutil.virtual_memory()[2])
            self.lb_ram_usavel.setText(
                str(f'{round(ram_usada_perc)} %'))

        # Barras de stilo da memoria RAM:
            self.ram_used.spb_setMinimum((0, 0, 0))

            self.ram_used.spb_setMaximum((total_ram, total_ram, total_ram))
            self.ram_used.spb_setValue((ram_usada, ram_disp, ram_livre))
            self.ram_used.spb_lineColor(
                ((255, 56, 56), (56, 255, 69), (56, 210, 255)))
            self.ram_used.spb_setInitialPos(('West', 'West', 'West'))
            self.ram_used.spb_lineWidth(10)
            self.ram_used.spb_lineStyle(
                ('SolidLine', 'SolidLine', 'SolidLine'))
            self.ram_used.spb_lineCap(('RoundCap', 'RoundCap', 'RoundCap'))
            self.ram_used.spb_setPathHidden(True)

        # configurando dados sobre CPU:
            core = psutil.cpu_count(logical=True)
            self.lb_cpu_threads.setText(str(core))

            core_perc = psutil.cpu_percent()
            self.lb_cpu_uso.setText(f'{core_perc} %')

            core_nucleos = psutil.cpu_count(logical=False)
            self.lb_cpu_nucleos.setText(f'{core_nucleos}')

        # Barras de stilo da CPU:

            self.cpu_used.rpb_setMaximum(100)
            self.cpu_used.rpb_setValue(core_perc)
            self.cpu_used.rpb_setTextFont('Arial')
            self.cpu_used.rpb_setBarStyle('Hybrid2')
            self.cpu_used.rpb_setLineColor((41, 235, 253))
            self.cpu_used.rpb_setPieColor((29, 96, 103, 1))

            self.cpu_used.rpb_setTextColor((255, 255, 200))
            self.cpu_used.rpb_setInitialPos('West')
            self.cpu_used.rpb_setTextFormat('Percentage')
            self.cpu_used.rpb_setLineWidth(15)
            self.cpu_used.rpb_setPathWidth(15)
            self.cpu_used.rpb_setLineCap('RoundCap')

            sleep(1)
##############################################################################

##############################################################################
# Configurando painel Informações do Sistema:

    def system_info(self):
        timer = datetime.now().strftime('%I:%M:%S %p \n%H:%M:%S ')
        self.lb_sys_hora.setText(str(timer))
        dater = datetime.now().strftime('%d/%m/%Y')
        self.lb_sys_data.setText(str(dater))

        self.lb_sys_machin.setText(platform.machine())
        self.lb_sys_version.setText(platform.version())
        self.lb_sys_platafor.setText(platform.platform())
        self.lb_sys_sistema.setText(platform.system())
        self.lb_sys_cpu.setText(platform.processor())

##############################################################################

##############################################################################
# Configurando painel Atividades (Tabela):

        """       
        # Função para para preencher a tabela com os dados obtidos na função processo()
        # Função recebe : O número da linda, número da coluna, O conteudo e o nome da tabela
        
        # 
         
        # PYTHON | MÉTODO GETATTR()
        getattr()
        A função é usada para acessar o valor do atributo de um objeto 
        e também dá a opção de executar o valor padrão em caso de indisponibilidade da chave. 
        Este tem maior aplicação para verificar as chaves disponíveis no desenvolvimento web 
        e muitas outras fases da programação do dia-a-dia.

        Sintaxe: getattr (obj, key, def)

        Parâmetros:
        obj: O objeto cujos atributos precisam ser processados.
        chave: O atributo do objeto
        def: O valor padrão que precisa ser impresso caso o atributo não seja encontrado.

        Retorna:
        Valor do objeto se o valor estiver disponível, valor padrão caso o atributo não esteja presente
        e retorna AttributeError caso o atributo não esteja presente e o valor padrão não seja
        especificado.
        # 
        #
        # Nesse caso:
        # getattr(self, table) == self.table_Activi
        """

    def criar_tabela_w(self, position_row, position_column, text, table):
        qtTabela = QTableWidgetItem()
        getattr(self, table).setItem(position_row, position_column, qtTabela)

        qtTabela = getattr(self, table).item(position_row, position_column)

        qtTabela.setText(text)

        """       
        # Função para buscar os processos em execução no maquina(PC/CPU)
        #   for x in psutil.pids() => laço para encontra o "id" dos processos
        #       processo = psutil.Process(x) => Setando cada processo individualmente
        #       E Usando o variavel "processo" para preencher a tabela,
        """

    def processos(self):
        for x in psutil.pids():
            position_row = self.table_Activi.rowCount()
            self.table_Activi.insertRow(position_row)

            try:
                processo = psutil.Process(x)

                self.criar_tabela_w(position_row, 0, str(
                    processo.pid), 'table_Activi')
                self.criar_tabela_w(position_row, 1, str(
                    processo.name()), 'table_Activi')
                self.criar_tabela_w(position_row, 2, str(
                    processo.status()), 'table_Activi')
                self.criar_tabela_w(position_row, 3, str(
                    datetime.utcfromtimestamp(processo.create_time()).strftime('%d/%m/%Y %H:%M:%S')), 'table_Activi')

            except:
                pass

        self.le_search_activ.textChanged.connect(self.encontrar_dado)

    def encontrar_dado(self):
        nome = self.le_search_activ.text().lower()
        for r in range(self.table_Activi.rowCount()):
            item = self.table_Activi.item(r, 1)
            self.table_Activi.setRowHidden(r, nome not in item.text().lower())
##############################################################################

##############################################################################
# Configurando painel Atividades (Tabela):

    def armazenamento(self):
        storage_device = psutil.disk_partitions(all=False)
        c = 0
        for x in storage_device:
            prosition_r = self.table_storage.rowCount()

            self.table_storage.insertRow(prosition_r)

            self.criar_tabela_w(prosition_r, 0, x.device, "table_storage")
            self.criar_tabela_w(prosition_r, 1, x.mountpoint, "table_storage")
            self.criar_tabela_w(prosition_r, 2, x.fstype, "table_storage")
            self.criar_tabela_w(prosition_r, 3, x.opts, "table_storage")

            if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':
                self.criar_tabela_w(prosition_r, 4, str(
                    x.maxfile), 'table_storage')
                self.criar_tabela_w(prosition_r, 5, str(
                    x.maxpath), 'table_storage')

            else:
                self.criar_tabela_w(prosition_r, 4, "Not info " +
                                    sys.platform, 'table_storage')
                self.criar_tabela_w(prosition_r, 5, "Not info " +
                                    sys.platform, 'table_storage')

            usoDisk = shutil.disk_usage(x.mountpoint)
            def calcule(x): return x / (1024*1024*1024)
            self.criar_tabela_w(prosition_r, 6, str(
                calcule(usoDisk.total))+" GB", "table_storage")
            self.criar_tabela_w(prosition_r, 7, str(
                calcule(usoDisk.free))+" GB", "table_storage")
            self.criar_tabela_w(prosition_r, 8, str(
                calcule(usoDisk.used))+" GB", "table_storage")

            full_disc = (usoDisk.used / usoDisk.total) * 100

            bar_progresso = QProgressBar(self.table_storage)
            bar_progresso.setObjectName(u"bar_progresso")
            bar_progresso.setValue(full_disc)
            self.table_storage.setCellWidget(prosition_r, 9, bar_progresso)


##############################################################################
# Configurando painel NetWorks (Tabela):

    def painel_netWorks(self):
        net = psutil.net_if_stats()
        for x in psutil.net_if_stats():
            netWork = net[x]

            prosition_r = self.tabela_Net_status.rowCount()

            self.tabela_Net_status.insertRow(prosition_r)

            self.criar_tabela_w(
                prosition_r, 0, f"{x}", "tabela_Net_status")
            self.criar_tabela_w(
                prosition_r, 1, str(netWork.isup), "tabela_Net_status")
            self.criar_tabela_w(
                prosition_r, 2, str(netWork.duplex), "tabela_Net_status")
            self.criar_tabela_w(
                prosition_r, 3, str(netWork.speed), "tabela_Net_status")
            self.criar_tabela_w(
                prosition_r, 4, str(netWork.mtu), "tabela_Net_status")

        net_io_v = psutil.net_io_counters(pernic=True)
        for i in psutil.net_io_counters(pernic=True):
            net_io = net_io_v[i]

            prosition_r = self.tabela_Net_IO.rowCount()

            self.tabela_Net_IO.insertRow(prosition_r)

            self.criar_tabela_w(
                prosition_r, 0, f"{i}", "tabela_Net_IO")
            self.criar_tabela_w(
                prosition_r, 1, str(net_io.bytes_sent), "tabela_Net_IO")
            self.criar_tabela_w(
                prosition_r, 2, str(net_io.bytes_recv), "tabela_Net_IO")
            self.criar_tabela_w(
                prosition_r, 3, str(net_io.packets_sent), "tabela_Net_IO")
            self.criar_tabela_w(
                prosition_r, 4, str(net_io.packets_recv), "tabela_Net_IO")
            self.criar_tabela_w(
                prosition_r, 5, str(net_io.errin), "tabela_Net_IO")
            self.criar_tabela_w(
                prosition_r, 6, str(net_io.errout), "tabela_Net_IO")
            self.criar_tabela_w(
                prosition_r, 7, str(net_io.dropin), "tabela_Net_IO")
            self.criar_tabela_w(
                prosition_r, 8, str(net_io.dropout), "tabela_Net_IO")

        for x in psutil.net_if_addrs().items():
            nome_net = x[0]
            for dado in x[1]:

                prosition_r = self.tabela_Net_addres.rowCount()

                self.tabelprosition_r = self.tabela_Net_addres.insertRow(
                    prosition_r)

                self.criar_tabela_w(
                    prosition_r, 0, f"{nome_net}", "tabela_Net_addres")
                self.criar_tabela_w(
                    prosition_r, 1, str(dado.family), "tabela_Net_addres")
                self.criar_tabela_w(
                    prosition_r, 2, str(dado.address), "tabela_Net_addres")
                self.criar_tabela_w(
                    prosition_r, 3, str(dado.netmask), "tabela_Net_addres")
                self.criar_tabela_w(
                    prosition_r, 4, str(dado.broadcast), "tabela_Net_addres")
                self.criar_tabela_w(
                    prosition_r, 5, str(dado.ptp), "tabela_Net_addres")

            net_conex = psutil.net_connections()
            for nets in net_conex:

                prosition_r = self.tabela_Net_connects.rowCount()

                self.tabelprosition_r = self.tabela_Net_connects.insertRow(
                    prosition_r)

                self.criar_tabela_w(
                    prosition_r, 0, str(nets[0]), "tabela_Net_connects")
                self.criar_tabela_w(
                    prosition_r, 1, str(nets[1]), "tabela_Net_connects")
                self.criar_tabela_w(
                    prosition_r, 2, str(nets[2]), "tabela_Net_connects")
                self.criar_tabela_w(
                    prosition_r, 3, str(nets[3]), "tabela_Net_connects")
                self.criar_tabela_w(
                    prosition_r, 4, str(nets[4]), "tabela_Net_connects")
                self.criar_tabela_w(
                    prosition_r, 5, str(nets[5]), "tabela_Net_connects")
                self.criar_tabela_w(
                    prosition_r, 6, str(nets[6]), "tabela_Net_connects")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TelManage()
    window.show()
    sys.exit(app.exec_())


"""
CONVERTER ARQUIVOS (.UI, .QRC)

>>> pyrcc5 -o icos_img_rc.py icos_img.qrc
E:\PROJESTOS_ADS\Py_Info_System\icons>pyrcc5 -o img_fundo_rc.py img_fundo.qrc
E:\PROJESTOS_ADS\Py_Info_System\icons>pyrcc5 -o icos_rc.py icos.qrc


import icons.icos_rc
import icons.img_fundo_rc

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets

> Para algumas coisas funcionarem tem que adicionar o PyDSide2 e PySide2Extn
import psutil
import PySide2extn
pip install  psutil
pip install  PySide2
pip install  PySide2Extn

>>> pyuic5 -x windows.ui -o windows.py

"""
