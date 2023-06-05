from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QColorDialog
from PySide6.QtCore import QUrl, QSize, QThreadPool, Qt, QTimer
from PySide6.QtGui import QIcon, QActionGroup, QColor
from PySide6.QtSerialPort import QSerialPortInfo
from UI_mainwindow import Ui_MainWindow
from musicPlayer import MusicPlayer
from spectrumAnalyzer import SpectrumAnalyzer
from usbSerial import UsbSerial
from worker import Worker

MAX_VOLUME_POS = 100
CHUNKS_SIZE = 4096 # sample
N_FFT = 4096
PERIOD_SCALE = 10

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.threadpool = QThreadPool()

        # Signals
        self.actionQuit.triggered.connect(self.quit)
        self.actionAbout.triggered.connect(self.show_information)

        """
        # Music Player
        """
        self.player = MusicPlayer()
        self.muted = False
        self.volume = 1
        self.horizontalSliderPlayer.setSliderPosition(0)
        self.toolButtonPlay.setEnabled(False)
        self.horizontalSliderVolume.setMaximum(MAX_VOLUME_POS)
        self.horizontalSliderVolume.setSliderPosition(MAX_VOLUME_POS)
        self.player.setVolume(self.volume)
        self.statusbar.showMessage("No files have been opened yet")
        self.setAcceptDrops(True)

        # Signals
        self.actionOpen_Music.triggered.connect(self.open_music)
        self.toolButtonPlay.clicked.connect(self.play_handler)
        self.toolButtonPause.clicked.connect(self.pause_handler)
        self.toolButtonStop.clicked.connect(self.stop_handler)
        self.horizontalSliderPlayer.sliderMoved.connect(self.change_sliderPlayer_position)
        self.horizontalSliderVolume.sliderMoved.connect(self.change_sliderPlayer_volume)
        self.toolButtonVolume.clicked.connect(self.toggle_mute)

        self.player.positionChanged.connect(self.change_player_position)
        self.player.durationChanged.connect(self.change_player_duration)

        """
        # Spectrum Analyser
        """
        self.spectrumAnalyzer = SpectrumAnalyzer(
            chunkSize=CHUNKS_SIZE,
            nFft=N_FFT
        )
        self.spectrumTimeout = int(self.spectrumAnalyzer.get_period() / PERIOD_SCALE)
        self.spectrumTimer = QTimer()  # Timer for updating index
        self.spectrumPosition = 0

        # Signals
        self.spectrumTimer.timeout.connect(self.update_spectrum_postion)

        """
        # USB Serial Interface
        """
        self.usbSerial = UsbSerial()
        self.usbSerial.configure(
            baudrate = UsbSerial.Baud115200,
            dataBits =  UsbSerial.Data8,
            parity = UsbSerial.NoParity,
            stopBits = UsbSerial.OneStop,
            flowControl = UsbSerial.NoFlowControl
        )
        self.portInfo = QSerialPortInfo()
        self.isConnected = False

        self.comActionGroup = QActionGroup(self.menuPort)
        self.comActionGroup.addAction(self.actionAvailablePort)
        self.comActionGroup.addAction(self.action_COM1)
        self.comActionGroup.addAction(self.action_COM2)
        self.comActionGroup.addAction(self.action_COM3)
        self.comActionGroup.addAction(self.action_COM4)
        self.comActionGroup.addAction(self.action_COM5)
        self.comActionGroup.addAction(self.action_COM6)
        self.comActionGroup.addAction(self.action_COM7)
        self.comActionGroup.addAction(self.action_COM8)
        self.comActionGroup.addAction(self.action_COM9)
        self.comActionGroup.addAction(self.action_COM10)
        self.comActionGroup.addAction(self.action_COM11)
        self.comActionGroup.addAction(self.action_COM12)
        self.comActionGroup.addAction(self.action_COM13)
        self.comActionGroup.addAction(self.action_COM14)
        self.comActionGroup.addAction(self.action_COM15)
        self.comActionGroup.addAction(self.action_COM16)
        self.comActionGroup.addAction(self.action_COM17)
        self.comActionGroup.addAction(self.action_COM18)
        self.comActionGroup.addAction(self.action_COM19)
        self.comActionGroup.addAction(self.action_COM20)
        self.comActionGroup.addAction(self.action_COM21)
        self.comActionGroup.addAction(self.action_COM22)
        self.comActionGroup.addAction(self.action_COM23)
        self.comActionGroup.addAction(self.action_COM24)
        self.comActionGroup.addAction(self.action_COM25)
        self.comActionGroup.addAction(self.action_COM26)
        self.comActionGroup.addAction(self.action_COM27)
        self.comActionGroup.addAction(self.action_COM28)
        for action in self.comActionGroup.actions():
            action.setCheckable(True)
        self.actionAvailablePort.setChecked(True)
        self.comActionGroup.setExclusive(True)

        self.modeActionGroup = QActionGroup(self.menuMode)
        self.modeActionGroup.addAction(self.actionMode_1)
        self.modeActionGroup.addAction(self.actionMode_2)
        self.modeActionGroup.addAction(self.actionMode_3)
        self.modeActionGroup.addAction(self.actionMode_4)
        self.modeActionGroup.addAction(self.actionMode_5)
        for action in self.modeActionGroup.actions():
            action.setCheckable(True)
        self.actionMode_1.setChecked(True)
        self.modeActionGroup.setExclusive(True)

        self.primaryColor = QColor(30, 129, 176)
        self.secondaryColor = QColor(108, 37, 190)
        self.tertiaryColor = QColor(190, 169, 37)
        self.primaryColorChanged = True
        self.secondaryColorChanged = True
        self.tertiaryColorChanged = True

        #Signals
        self.actionConnect.triggered.connect(self.connect_handler)
        self.usbSerial.readyRead.connect(self.receive_data)
        self.actionPrimaryColor.triggered.connect(self.open_primaryColor_dialog)
        self.actionSecondaryColor.triggered.connect(self.open_secondaryColor_dialog)
        self.actionTertiaryColor.triggered.connect(self.open_tertiaryColor_dialog)

    ########################################
    #        Functions and Slots           #
    ########################################
    def open_music(self):
        path, _ = QFileDialog.getOpenFileName(
            self, 
            'Open Music',
            './',
            'Audio (*.wav *.mp3)'
        )
        if path != '':
            self.load_music(path)

    def load_music(self, path):
        self.statusbar.showMessage("File is loading...")
        self.player.setSource(QUrl.fromLocalFile(path))
        self.setWindowTitle('Mspezer - ' + path.split('/')[-1])
        self.createChunks = Worker(self.spectrumAnalyzer.create_chunks, path)
        self.createChunks.signals.finished.connect(self.create_chunks_successed)
        self.createChunks.signals.error.connect(self.create_chunks_failed)
        self.threadpool.start(self.createChunks)

    def create_chunks_successed(self):
        self.toolButtonPlay.setEnabled(True)
        self.stop_handler()
        self.statusbar.showMessage("File loaded successfully", 5000)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, e):
        """
        Drop files directly onto the widget
        File locations are stored in fname
        :param e:
        :return:
        """
        if not e.mimeData().hasUrls():
            e.ignore()
            return

        e.setDropAction(Qt.CopyAction)
        e.acceptProposedAction()
        urlList =  e.mimeData().urls()
        path = str(urlList[0].toLocalFile())
        pathExtension  = path.split('.')[-1]
        if pathExtension == 'mp3' or pathExtension == 'wav':
            self.load_music(path)

    def create_chunks_failed(self):
        self.statusbar.showMessage("File loading failed!")

    def quit(self):
        self.app.quit()

    def closeEvent(self, event):
        self.usbSerial.close_port()

    def show_information(self):
        QMessageBox.information(
            self, 
            "About MSpezer",
            "A desktop application to play music, display spectrum visuallly and control matrix rgb LED according to music(>.<)", 
            QMessageBox.Ok
        )

    def connect_handler(self):
        if self.isConnected:
            self.usbSerial.close_port()
            self.isConnected = False
            self.set_enable_tools(True)
            self.actionConnect.setToolTip('Connect')
            self.statusbar.showMessage('Diconnect successfully!!!', 5000)
            self.actionConnect.setIcon(QIcon(':/images/connect.png'))
            return

        _checkedAction = self.comActionGroup.checkedAction()
        if _checkedAction == self.actionAvailablePort:
            _portInfoList = QSerialPortInfo.availablePorts()
            if (len(_portInfoList) != 0):
                self.portInfo = _portInfoList[0]
                print(self.portInfo.portName())
                self.usbSerial.setPort(self.portInfo)
            else:
                self.statusbar.showMessage('No ports available!!!', 5000)
                return
        else:
            portName = _checkedAction.text()
            self.usbSerial.setPortName(portName)

        if self.usbSerial.open_port():
            self.isConnected = True
            self.set_enable_tools(True)
            self.primaryColorChanged = True;
            self.secondaryColorChanged = True;
            self.tertiaryColorChanged = True;
            self.actionConnect.setToolTip('Disconnect')
            self.statusbar.showMessage('Connect successfully!!!', 5000)
            self.actionConnect.setIcon(QIcon(':/images/disconnect.png'))
        else:
            self.statusbar.showMessage("Connect failed!!!", 5000)

    def set_enable_tools(self, enable):
        self.actionConnect.setEnabled(enable)
        comActionsEnable = enable and (not self.isConnected)
        for action in self.comActionGroup.actions():
            action.setEnabled(comActionsEnable)

    def play_handler(self):
        if self.player.playbackState() != MusicPlayer.PlayingState:
            self.player.play()
            self.set_enable_tools(False)
            self.toolButtonPlay.setStyleSheet('background-color: rgb(172,172,172);padding: 10px;border-radius: 6px;')
            self.toolButtonStop.setStyleSheet('background-color: rgb(204,204,204);padding: 10px;border-radius: 6px;')
            self.toolButtonPause.setStyleSheet('background-color: rgb(204,204,204);padding: 10px;border-radius: 6px;')

    def pause_handler(self):
        if self.player.playbackState != MusicPlayer.PausedState and self.player.PlaybackState != MusicPlayer.StoppedState:
            self.player.pause()
            self.set_enable_tools(True)
            if self.spectrumTimer.isActive():
                self.spectrumTimer.stop()
            self.toolButtonPause.setStyleSheet('background-color: rgb(172,172,172);padding: 10px;border-radius: 6px;')
            self.toolButtonStop.setStyleSheet('background-color: rgb(204,204,204);padding: 10px;border-radius: 6px;')
            self.toolButtonPlay.setStyleSheet('background-color: rgb(204,204,204);padding: 10px;border-radius: 6px;')

    def stop_handler(self):
        if self.player.playbackState != MusicPlayer.StoppedState:
            self.player.stop()
            self.spectrumAnalyzer.reset_index()
            self.set_enable_tools(True)
            if self.spectrumTimer.isActive():
                self.spectrumTimer.stop()
            self.toolButtonStop.setStyleSheet('background-color: rgb(172,172,172);padding: 10px;border-radius: 6px;')
            self.toolButtonPause.setStyleSheet('background-color: rgb(204,204,204);padding: 10px;border-radius: 6px;')
            self.toolButtonPlay.setStyleSheet('background-color: rgb(204,204,204);padding: 10px;border-radius: 6px;')

            self.progressBar_Spectrum1.setValue(0)
            self.progressBar_Spectrum2.setValue(0)
            self.progressBar_Spectrum3.setValue(0)
            self.progressBar_Spectrum4.setValue(0)
            self.progressBar_Spectrum5.setValue(0)
            self.progressBar_Spectrum6.setValue(0)
            self.progressBar_Spectrum7.setValue(0)
            self.progressBar_Spectrum8.setValue(0)

    def change_sliderPlayer_position(self, position):
        self.player.setPosition(position)

    def change_player_position(self, position):
        self.horizontalSliderPlayer.setValue(position)
        self.labelPosition.setText(self.mmss(position))
        if position == self.player.duration():
            self.stop_handler()

        self.handle_spectrum(position)

        if self.spectrumTimer.isActive():
            self.spectrumTimer.stop()
        if self.player.playbackState() == MusicPlayer.PlayingState:
            self.spectrumPosition = position
            self.spectrumTimer.start(self.spectrumTimeout)

    def handle_spectrum(self, position):
        # print(position)
        if (self.spectrumAnalyzer.update_index(position)):
            self.cal_magnitude_levels = Worker(self.spectrumAnalyzer.cal_magnitude_levels)
            self.cal_magnitude_levels.signals.result.connect(self.result_handler)
            self.threadpool.start(self.cal_magnitude_levels)

    def update_spectrum_postion(self):
        self.spectrumPosition += self.spectrumTimeout
        self.handle_spectrum(self.spectrumPosition)

    def result_handler(self, magnitudeLevels):
        # Magnitude level
        magnitudeLevels = list(magnitudeLevels)
        # print(magnitudeLevels)

        # Mode 
        for i, x in enumerate(self.modeActionGroup.actions()):
            if x.isChecked():
                self.modeSelected = i + 1
                break

        # Color
        if self.primaryColorChanged:
            self.colorTypeSelected = 1
            self.currentColorSlected = self.primaryColor
            self.primaryColorChanged = False   
        elif self.secondaryColorChanged:
            self.colorTypeSelected = 2
            self.currentColorSlected = self.secondaryColor
            self.secondaryColorChanged = False 
        elif self.tertiaryColorChanged:
            self.colorTypeSelected = 3
            self.currentColorSlected = self.tertiaryColor
            self.tertiaryColorChanged = False
        else:
            self.colorTypeSelected = 0
            self.currentColorSlected = QColor(0, 0, 0)

        # Send data to virtual COM port
        self.send_data(
            self.colorTypeSelected,
            self.modeSelected,
            magnitudeLevels,
            self.currentColorSlected
        )

        # Update progress bar
        self.update_progress_bar(magnitudeLevels)

    def send_data(self, colorTypeSelected, modeSelected, magnitudeLevels, currentColorSelected):
        if not self.usbSerial.isOpen():
            return
        package = []
        package.append(self.pack_byte(modeSelected, colorTypeSelected))
        for i in range(0, len(magnitudeLevels), 2):
            package.append(self.pack_byte(magnitudeLevels[i], magnitudeLevels[i+1]))
        package.append(currentColorSelected.red())
        package.append(currentColorSelected.green())
        package.append(currentColorSelected.blue())

        self.usbSerial.write(bytes(package))

    def receive_data(self):
        dataRecieved = self.usbSerial.readAll()
        dataRecieved = dataRecieved.toHex()
        print(f"{dataRecieved}\n")

    def change_player_duration(self, duration):
        # print(duration)
        self.horizontalSliderPlayer.setRange(0, duration)
        self.labelDuration.setText(self.mmss(duration))

    def change_sliderPlayer_volume(self, position):
        self.volume = position / MAX_VOLUME_POS
        self.player.setVolume(self.volume)
        if self.volume == 0:
            self.muted = True
            self.set_icon_resize(
                self.toolButtonVolume,
                ':/images/volume-mute.png',
                24,
                24
            )
        elif self.volume <= 0.5:
            self.set_icon_resize(
                self.toolButtonVolume,
                ':/images/low-volume.png',
                28,
                28
            )
        else:
            self.set_icon_resize(
                self.toolButtonVolume,
                ':/images/medium-volume.png',
                28,
                28
            )

    def toggle_mute(self):
        if not self.muted:
            self.player.setMuted(True)
            self.muted = True
            self.horizontalSliderVolume.setValue(0)
            self.set_icon_resize(
                self.toolButtonVolume,
                ':/images/volume-mute.png',
                24,
                24
            )
        else:
            self.player.setMuted(False)
            self.muted = False
            if (self.volume == 0):
                self.volume = 0.6
            self.player.setVolume(self.volume)
            self.horizontalSliderVolume.setValue(self.volume * MAX_VOLUME_POS)
            if self.volume <= 0.5:
                self.set_icon_resize(
                    self.toolButtonVolume,
                    ':/images/low-volume.png',
                    28,
                    28
                )
            else:
                self.set_icon_resize(
                    self.toolButtonVolume,
                    ':/images/medium-volume.png',
                    28,
                    28
                )

    def update_progress_bar(self, magnitudeLevels):
        self.progressBar_Spectrum1.setValue(magnitudeLevels[0])
        self.progressBar_Spectrum2.setValue(magnitudeLevels[1])
        self.progressBar_Spectrum3.setValue(magnitudeLevels[2])
        self.progressBar_Spectrum4.setValue(magnitudeLevels[3])
        self.progressBar_Spectrum5.setValue(magnitudeLevels[4])
        self.progressBar_Spectrum6.setValue(magnitudeLevels[5])
        self.progressBar_Spectrum7.setValue(magnitudeLevels[6])
        self.progressBar_Spectrum8.setValue(magnitudeLevels[7])

    def open_primaryColor_dialog(self):
        colorDialog = QColorDialog(self.primaryColor,self)
        colorDialog.colorSelected.connect(self.change_primaryColor)
        colorDialog.open()

    def change_primaryColor(self, color):
        self.primaryColor = color
        self.primaryColorChanged = True

    def open_secondaryColor_dialog(self):
        colorDialog = QColorDialog(self.secondaryColor,self)
        colorDialog.colorSelected.connect(self.change_secondaryColor)
        colorDialog.open()

    def change_secondaryColor(self, color):
        self.secondaryColor = color
        self.secondaryColorChanged = True

    def open_tertiaryColor_dialog(self):
        colorDialog = QColorDialog(self.tertiaryColor,self)
        colorDialog.colorSelected.connect(self.change_tertiaryColor)
        colorDialog.open()

    def change_tertiaryColor(self, color):
        self.tertiaryColor = color
        self.tertiaryColorChanged = True

    def mmss(self, ms):
        s = round(ms / 1000) % 60
        m = round(ms / 1000) / 60
        return ("%02d:%02d" % (m, s))
    
    def set_icon_resize(self, object, path, width, height):
        object.setIcon(QIcon(path))
        object.setIconSize(QSize(width, height))

    def pack_byte(self, highNibble, lowNibble):
        if highNibble > 15 or lowNibble > 15:
            return -1
        return (highNibble << 4) | lowNibble